let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

const taskInput = document.getElementById("taskInput");
const addTask = document.getElementById("addTask");
const taskList = document.getElementById("taskList");

const totalTasks = document.getElementById("totalTasks");
const completedTasks = document.getElementById("completedTasks");
const pendingTasks = document.getElementById("pendingTasks");

const clearCompleted = document.getElementById("clearCompleted");

function saveTasks() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function updateStats() {
    totalTasks.textContent = tasks.length;

    completedTasks.textContent =
        tasks.filter(task => task.completed).length;

    pendingTasks.textContent =
        tasks.filter(task => !task.completed).length;
}

function renderTasks() {

    taskList.innerHTML = "";

    tasks.forEach(task => {

        const li = document.createElement("li");
        li.className = "task-item";

        li.innerHTML = `
            <span class="task-text ${task.completed ? "completed" : ""}">
                ${task.text}
            </span>

            <div class="task-buttons">

                <button class="complete-btn" data-id="${task.id}">
                    ${task.completed ? "Undo" : "Complete"}
                </button>

                <button class="edit-btn" data-id="${task.id}">
                    Edit
                </button>

                <button class="delete-btn" data-id="${task.id}">
                    Delete
                </button>

            </div>
        `;

        taskList.appendChild(li);

    });

    updateStats();
    saveTasks();
    attachEvents();
}

function attachEvents() {

    document.querySelectorAll(".complete-btn").forEach(button => {

        button.addEventListener("click", function () {

            const id = Number(this.dataset.id);

            const task = tasks.find(task => task.id === id);

            task.completed = !task.completed;

            renderTasks();

        });

    });

    document.querySelectorAll(".edit-btn").forEach(button => {

        button.addEventListener("click", function () {

            const id = Number(this.dataset.id);

            const task = tasks.find(task => task.id === id);

            const newText = prompt("Edit Task", task.text);

            if (newText && newText.trim() !== "") {

                task.text = newText.trim();

                renderTasks();

            }

        });

    });

    document.querySelectorAll(".delete-btn").forEach(button => {

        button.addEventListener("click", function () {

            const id = Number(this.dataset.id);

            tasks = tasks.filter(task => task.id !== id);

            renderTasks();

        });

    });

}

addTask.addEventListener("click", function () {

    const text = taskInput.value.trim();

    if (text === "") {

        alert("Please enter a task.");
        return;

    }

    tasks.push({

        id: Date.now(),
        text: text,
        completed: false

    });

    taskInput.value = "";

    renderTasks();

});

taskInput.addEventListener("keypress", function (event) {

    if (event.key === "Enter") {

        addTask.click();

    }

});

clearCompleted.addEventListener("click", function () {

    tasks = tasks.filter(task => !task.completed);

    renderTasks();

});

renderTasks();