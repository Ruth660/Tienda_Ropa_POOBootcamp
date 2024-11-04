<template>
  <div class="container mt-5">
    <div class="text-center">
      <h1><strong>Aplicación de tareas con Vue</strong></h1>
      <p class="lead text-secondary mb-4">
        Gestiona tus tareas de manera eficiente. Agrega nuevas tareas o visualiza las existentes.
      </p>
      <img src="@/assets/logo.png" class="img-fluid mb-4 logo" alt="Vue logo" />
      <h2>Secciones de la aplicación</h2>
      <div class="list-group text-start">
        <a class="list-group-item list-group-item-action text-white bg-success">
          Añadir tarea: Permite añadir nuevas tareas.
        </a>
        <a class="list-group-item list-group-item-action text-white bg-success">
          Lista de tareas: Muestra todas las tareas, con opciones para marcar como completadas o borrar.
        </a>
        <a class="list-group-item list-group-item-action text-white bg-success">
          Vista combinada: Visualiza y agrega tareas simultáneamente.
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>

<style scoped>
.container {
  max-width: 900px;
}

.lead {
  font-size: 25px;
}

.logo {
  border-radius: 50%; 
  box-shadow: 0 0 20px rgba(128, 128, 128, 0.5); 
}

h2 {
  font-weight: bold;
}

.text-muted {
  font-size: 1rem;
}
</style>