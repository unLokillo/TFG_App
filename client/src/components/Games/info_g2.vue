<template>
    <div class="card-body">
        <div>
      <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
       <h2>Información</h2>
       </div> 
       <p>
         ¡Este apartado todavia esta en construcción! Vuelve más adelante porfavor :) </p>
         <img src="@/assets/images/Under_construction.png" >
    <!--<b-button :to="{name: 'game_2',params: {}}" > ¡¡ Juega !! </b-button>-->
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
