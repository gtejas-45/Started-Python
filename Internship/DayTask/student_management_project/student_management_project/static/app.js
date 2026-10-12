const form = document.getElementById("studentForm");
const rows = document.getElementById("studentRows");
const message = document.getElementById("message");
const formTitle = document.getElementById("formTitle");
const submitButton = document.getElementById("submitButton");
const cancelButton = document.getElementById("cancelButton");

let editingRoll = null;
let students = {};

// Show messages returned by the backend.
function showMessage(text, type = "success") {
    message.textContent = text;
    message.className = `message ${type}`;
    window.clearTimeout(showMessage.timer);
    showMessage.timer = window.setTimeout(() => {
        message.className = "message hidden";
    }, 4500);
}

async function apiRequest(url, options = {}) {
    const response = await fetch(url, {
        ...options,
        headers: {
            "Content-Type": "application/json",
            ...(options.headers || {})
        }
    });

    const data = await response.json().catch(() => ({}));

    if (!response.ok) {
        throw new Error(data.detail || "Something went wrong. Please try again.");
    }
    return data;
}

function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, character => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#039;"
    })[character]);
}

// Get the latest records from the JSON file through FastAPI.
async function loadStudents() {
    try {
        students = await apiRequest("/get_student");
        renderStudents();
    } catch (error) {
        rows.innerHTML = `<tr><td colspan="6" class="empty">${escapeHtml(error.message)}</td></tr>`;
        showMessage(error.message, "error");
    }
}

function renderStudents() {
    const entries = Object.entries(students).sort((a, b) => Number(a[0]) - Number(b[0]));
    document.getElementById("totalCount").textContent = entries.length;
    document.getElementById("placedCount").textContent =
        entries.filter(([, student]) => student.Placed === true).length;

    if (entries.length === 0) {
        rows.innerHTML = '<tr><td colspan="6" class="empty">No students yet. Add the first student using the form.</td></tr>';
        return;
    }

    rows.innerHTML = entries.map(([roll, student]) => `
        <tr>
            <td>${escapeHtml(roll)}</td>
            <td><strong>${escapeHtml(student.Name)}</strong></td>
            <td>${escapeHtml(student.Marks)}</td>
            <td>${escapeHtml(student.Address)}</td>
            <td><span class="status ${student.Placed ? "yes" : "no"}">${student.Placed ? "Placed" : "Not placed"}</span></td>
            <td>
                <div class="row-actions">
                    <button class="action-button" type="button" data-action="edit" data-roll="${escapeHtml(roll)}">Edit</button>
                    <button class="action-button delete" type="button" data-action="delete" data-roll="${escapeHtml(roll)}">Delete</button>
                </div>
            </td>
        </tr>
    `).join("");
}

function resetForm() {
    form.reset();
    document.getElementById("placed").value = "true";
    document.getElementById("roll").disabled = false;
    editingRoll = null;
    formTitle.textContent = "Add a student";
    submitButton.textContent = "Add student";
    cancelButton.classList.add("hidden");
}

form.addEventListener("submit", async event => {
    event.preventDefault();

    const payload = {
        roll: Number(document.getElementById("roll").value),
        name: document.getElementById("name").value.trim(),
        marks: Number(document.getElementById("marks").value),
        address: document.getElementById("address").value.trim(),
        placed: document.getElementById("placed").value === "true"
    };

    try {
        if (editingRoll === null) {
            await apiRequest("/add_student", {
                method: "POST",
                body: JSON.stringify(payload)
            });
            showMessage("Student added successfully.");
        } else {
            await apiRequest(`/edit_student/${editingRoll}`, {
                method: "PUT",
                body: JSON.stringify(payload)
            });
            showMessage("Student details updated successfully.");
        }

        resetForm();
        await loadStudents();
    } catch (error) {
        showMessage(error.message, "error");
    }
});

rows.addEventListener("click", async event => {
    const button = event.target.closest("button[data-action]");
    if (!button) return;

    const roll = button.dataset.roll;
    const student = students[roll];

    if (button.dataset.action === "edit") {
        if (!student) return;

        editingRoll = Number(roll);
        document.getElementById("roll").value = roll;
        document.getElementById("roll").disabled = true;
        document.getElementById("name").value = student.Name;
        document.getElementById("marks").value = student.Marks;
        document.getElementById("address").value = student.Address;
        document.getElementById("placed").value = String(student.Placed);
        formTitle.textContent = `Edit student ${roll}`;
        submitButton.textContent = "Save changes";
        cancelButton.classList.remove("hidden");
        document.getElementById("name").focus();
        return;
    }

    if (button.dataset.action === "delete") {
        if (!window.confirm(`Delete the record for ${student?.Name || "this student"} (roll ${roll})?`)) return;

        try {
            await apiRequest(`/delete_student/${roll}`, { method: "DELETE" });
            if (editingRoll === Number(roll)) resetForm();
            showMessage("Student deleted successfully.");
            await loadStudents();
        } catch (error) {
            showMessage(error.message, "error");
        }
    }
});

cancelButton.addEventListener("click", resetForm);
document.getElementById("refreshButton").addEventListener("click", loadStudents);

loadStudents();
