<template>
    <div class="container mt-4">
      <h1>Lista de tareas</h1>
      <div class="input-group mb-3">
        <input v-model="newTask" @keyup.enter="addTask" placeholder="Escribe aquí la nueva tarea"
          class="form-control task-input" aria-label="Nueva tarea" />
        <button @click="addTask" class="btn btn-success">
          <i class="bi bi-plus-circle me-2"></i><strong>Añadir</strong>
        </button>
      </div>
  
      <div class="row mt-4">
        <div class="col-12 mb-4" v-for="task in tasks" :key="task.id">
          <div class="task-card d-flex flex-column">
            <div class="d-flex justify-content-between align-items-center mb-2">
              <div class="flex-grow-1 me-2 text-start">
                <h5 class="m-0" :class="{ 'completed': task.completed }">
                  {{ task.todo }}
                </h5>
              </div>
              <span class="badge"
                :class="{ 'bg-success': task.completed, 'bg-warning text-black': !task.completed }">
                {{ task.completed ? 'Completada' : 'Pendiente' }}
              </span>
            </div>
            <div class="d-flex justify-content-center mt-auto">
              <button @click="toggleTaskCompletion(task)" class="btn btn-outline-success me-2"
                aria-label="Marcar como completada">
                <i :class="task.completed ? 'bi bi-check-circle-fill' : 'bi bi-check-circle'"></i>
              </button>
              <button @click="deleteTask(task.id)" class="btn btn-outline-danger"
                aria-label="Eliminar tarea">
                <i class="bi bi-trash"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "CombinedView",
    props: ['tasks'], 
    data() {
      return {
        newTask: "",
      };
    },
    methods: {
      addTask() {
        if (this.newTask.trim() === "") return;
  
        const newTask = {
          todo: this.newTask,
          completed: false,
          id: Date.now(), 
        };
  
        this.$emit('add-task', newTask); 
        this.newTask = ""; 
      },
      toggleTaskCompletion(task) {
        task.completed = !task.completed; 
      },
      deleteTask(taskId) {
        this.$emit('delete-task', taskId); 
      },
    },
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
    padding: 20px;
  }
  
  .task-input {
    flex-grow: 1;
    padding: 8px;
    border: 1px solid #000000;
    border-radius: 4px;
  }
  
  .task-card {
    background-color: #f1ff70; 
    color: #000000;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    margin-bottom: 15px;
  }
  
  .completed {
    text-decoration: line-through;
    color: gray;
  }
  
  .badge {
    font-size: 0.85em;
    padding: 5px 10px;
  }
  </style>
  