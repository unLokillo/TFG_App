<template>
  <div class="card-body">
    <div>
      <div class="close-modal">
        <a @click="$router.go(-1)">
          <font-awesome-icon style="font-size: 140%" icon="times" />
        </a>
      </div>
      <h2 style="border-bottom: 1px solid var(--border)">Información</h2>
    </div>
    <p>
      Term-fishing is an application that allows to capture, describe and 
      evaluate terms in the field of sustainability. It has been developed 
      as part of the educational innovation project "Gamification strategies 
      applied to the collaborative acquisition of scientific-technical 
      vocabulary in English and Spanish", developed by professors of the 
      Universidad Politécnica de Madrid. <br />
      <br />
      The main objective of this project is to motivate students of different 
      degrees of the UPM in the acquisition of scientific-technical 
      vocabulary in the field of sustainability in a collaborative and 
      playful way. 
      <br /><br />
      With the help of this fleet of "term fishermen and fisherwomen" we aim 
      to detect, analyse, evaluate and compile terms related to 
      sustainability on campus both in English and Spanish. 
      <br />
      <br />

      <strong style="align-content: center"> Coming fishing? </strong>
    </p>
    <div></div>
  </div>
</template>

<style scoped>
.card-body {
  background-color: var(--first-color);
  display: flex;
  padding: 4%;
  text-align: left;
  flex-direction: column;
  justify-content: space-between;
}
</style>
