<template>
    <div class="card-body">
        <div>
      <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
       <h2>Información</h2>
       </div> 
       <p>
         ¡Este apartado todavia esta en construcción! Vuelve más adelante porfavor :) </p>
         <div>
          <img style="width:50%;height:100%" src="@/assets/images/Under_construction.jpg" >
         </div>
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
