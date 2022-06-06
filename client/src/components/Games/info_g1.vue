<template>
  <div class="card-body">
    <div>
      <div class="close-modal">
        <a @click="$router.go(-1)">
          <font-awesome-icon style="font-size: 140%" icon="times" />
        </a>
      </div>
      <h1 style="color: #3481c0; margin-bottom: -5%">Sliding cards</h1>
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
      Welcome to this activity!<br />
      <p style="font-size: 15px; padding-top: 1%">
        Here you will select which are the best terms in the app.
      </p>
    </h5>
    <strong style="margin-top: -30px">
      <p style="color: darkgreen; text-align: left; padding-left: 13%;">
        - Slide the card to the right if <strong> YOU LIKE IT</strong>.
      </p>
      <br />
      <p style="color: darkred; text-align: left; padding-left: 13%">
        - Slide the card to the right if <strong> YOU DON'T LIKE IT ENOUGH</strong>.
      </p>
    </strong>
    <router-link :to="{ name: 'game_1' }" tag="b-button">
      Let's play !
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
