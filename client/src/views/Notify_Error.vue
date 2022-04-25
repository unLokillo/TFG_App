<template>
  <div class="reject-body">
    <div class="close-modal">
      <a @click="$router.go(-1)">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </a>
    </div>
    <h2>Notificar error</h2>
    <p>Por favor, cuéntanos qué ha pasado con el mayor detalle posible.</p>
    <b-form-textarea
      placeholder="Explicanos que ha pasado"
      rows="5"
      max-rows="150"
      class="reject-info"
    ></b-form-textarea>
    <b-button style="background-color: var(--success) !important">
      Aceptar
    </b-button>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
};
</script>

<style scoped>
h2 {
  border-bottom: 1px solid var(--fail);
  padding-bottom: 2%;
}

.reject-body {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 3%;
}

.reject-info {
  width: 100%;
  min-height: 50%;
  border: 2px solid var(--fail);
}
</style>
