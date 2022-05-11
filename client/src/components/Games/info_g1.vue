<template>
    <div class="card-body">
        <div>
      <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
       <h2>Cartas deslizantes</h2>
       </div> 
       <h5 style="border-bottom:1px solid var(--border);padding-bottom: 2%">¡Bienvenido a la actividad!</h5>
       <p> 
         Jugando podrás seleccionar cuáles son los Neologismos que te gustan más.
       <br>
       Para ello, sigue estas reglas: <br><br><strong>
       <p style="color:darkgreen; text-align: left; margin-left: 13%;">- Desliza la carta derecha si el Neologismo te gusta. </p><br>
       <p style="color:darkred; text-align: left; margin-left: 13%;">- Desliza la carta a la izquierda si el Neologismo no te interesa.</p>
        </strong>
       </p>
       <h5>       ¡Eso es todo, esperamos que disfrutes!</h5>
    <router-link :to="{name: 'game_1'}" tag="b-button"> ¡ A jugar ! </router-link>
    </div>     
</template>

<style scoped>
.card-body{
  background-color: var(--secondary-color);
  display: flex;
  padding: 4%;
  flex-direction: column;
  justify-content: space-between;
}

</style>
