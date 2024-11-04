<template>
    <div class="container mt-4">
        <h1 class="text-center text-black mb-4">Añadir tarea</h1>
        <div class="input-group mb-3">
            <input v-model="newTask" @keyup.enter="addTask" placeholder="Escribe aquí la tarea nueva"
                class="form-control task-input"/>
            <button @click="addTask" class="btn btn-success">
                <i class="bi bi-plus-circle me-2"></i><strong>Añadir</strong>
            </button>
        </div>
        
        <div class="row mt-4" v-if="addedTasks.length > 0">
            <div class="col-12 mb-4" v-for="task in addedTasks" :key="task.id">
                <div class="task-card d-flex flex-column">
                    <h5 class="d-flex justify-content-between align-items-center mb-2">
                        <div class="flex-grow-1 me-2 text-start">
                            <h5 class="m-0" :class="{ 'completed': task.completed }">
                                {{ task.todo }}
                            </h5>
                        </div>
                        <span class="badge"
                            :class="{ 'bg-success': task.completed, 'bg-warning text-black': !task.completed }">
                            {{ task.completed ? 'Completada' : 'Pendiente' }}
                        </span>
                    </h5>
                    <div class="d-flex justify-content-center mt-auto">
                        <div class="d-flex">
                            <button @click="toggleTaskCompletion(task)" class="btn btn-outline-success me-2"
                                aria-label="Marcar como completada">
                                <i :class="task.completed ? 'bi bi-check-circle-fill' : 'bi bi-check-circle'"></i>
                            </button>
                            <button @click="deleteTask(task)" class="btn btn-outline-danger"
                                aria-label="Eliminar tarea">
                                <i class="bi bi-trash"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  props: ['tasks'],
  data() {
    return {
      newTask: "",
      addedTasks: [], 
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

      this.addedTasks.push(newTask);
      this.$emit('add-task', newTask);
      this.newTask = ""; 
    },
    toggleTaskCompletion(task) {
      task.completed = !task.completed; 
    },
    deleteTask(task) {
      this.addedTasks = this.addedTasks.filter(t => t.id !== task.id); 
      this.$emit('delete-task', task.id); 
    },
  },
};
</script>

<style scoped>
.container {
    max-width: 800px;
}

.task-card {
    background-color: #f1ff70; 
    color: #000000; 
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    margin-bottom: 15px; 
}

.task-input {
    flex-grow: 1;
    padding: 8px;
    border: 1px solid #000000;
    border-radius: 4px;
  }

.completed {
    text-decoration: line-through;
    color: gray;
}
</style>
