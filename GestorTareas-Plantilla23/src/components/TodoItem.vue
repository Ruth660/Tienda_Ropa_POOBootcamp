: <template>
    <div class="todo-item">
       <h5 class="d-flex justify-content-between align-items-center">
           <span :class="{ 'completed': completed }">{{ title }}</span>
           <span class="badge" :class="{ 'bg-success': completed, 'bg-warning text-black': !completed }">
               {{ completed ? 'Completada' : 'Pendiente' }}
           </span>
       </h5>
       <div class="actions">
           <button @click="$emit('toggle-completion')" class="btn btn-outline-success">
               <i :class="completed ? 'bi bi-check-circle-fill' : 'bi bi-check-circle'"></i>
           </button>
           <button @click="$emit('delTodo')" class="btn btn-outline-danger">
               <i class="bi bi-trash-fill"></i>
           </button>
       </div>
   </div>
</template>

<script>
export default {
   
   name: 'TodoItem',

   props: {
       title: String,      
       completed: Boolean, 
   }
}
</script>

<style scoped>


.todo-item {
   display: flex;
   flex-direction: column;
   padding: 10px;
}

.completed {
   text-decoration: line-through;
   color: rgb(0, 148, 7);
}

.actions {
   margin-top: 10px;
}

.actions button {
   margin-left: 10px;
}
</style>