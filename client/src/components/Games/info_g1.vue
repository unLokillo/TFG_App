<template>
  <div class="card-body">
    <div>
      <div class="close-modal">
        <a @click="$router.go(-1)">
          <font-awesome-icon style="font-size: 140%" icon="times" />
        </a>
      </div>
      <h1 style="color: #3481c0; margin-bottom: -5%">Cartas deslizantes</h1>
    </div>
    <h5
      style="
        border-bottom: 1px solid var(--border);
        border-top: 1px solid var(--border);
        padding-bottom: 1%;
        padding-top: 2%;
        font-size: 20px;
      "
    >
      ¡Bienvenido a la actividad!<br />
      <p style="font-size: 15px; padding-top: 1%">
        Aquí podrás seleccionar cuáles son los Neologismos que te gustan más.
      </p>
    </h5>
    <strong style="margin-top: -30px">
      <p style="color: darkgreen; text-align: left; padding-left: 13%;">
        - Desliza la carta hacia la derecha si <strong> TE GUSTA</strong>.
      </p>
      <br />
      <p style="color: darkred; text-align: left; padding-left: 13%">
        - Desliza la carta hacia la izquierda si
        <strong> NO TE INTERESA</strong>.
      </p>
    </strong>
    <router-link :to="{ name: 'game_1' }" tag="b-button">
      ¡ A jugar !
    </router-link>
  </div>
</template>

<style scoped>
.card-body {
  background-color: var(--secondary-color);
  display: flex;
  padding: 4%;
  flex-direction: column;
  justify-content: space-between;
}
</style>
