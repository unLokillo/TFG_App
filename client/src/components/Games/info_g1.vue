<template>
    <div class="card-body">
        <div>
      <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
       <h2>Información</h2>
       </div> 
       <p>

Lorem ipsum dolor sit amet, consectetur adipiscing elit. In scelerisque orci non rutrum dictum. Mauris pharetra metus quis arcu accumsan volutpat. Mauris vel posuere massa. Aenean lobortis, erat et ornare tempor, erat diam venenatis quam, non volutpat purus purus a lectus. Sed laoreet augue et pulvinar porttitor. Maecenas facilisis, leo eget fermentum suscipit, elit dolor placerat nulla, efficitur vestibulum arcu nisi a massa. Morbi nibh libero, viverra a neque in, vestibulum blandit nibh. Nunc faucibus sodales felis at aliquam. Integer sodales enim ac placerat ullamcorper. Pellentesque mollis, urna et condimentum interdum, urna lorem finibus erat, at euismod lorem leo eu sapien. Mauris et sapien id enim convallis blandit. Fusce eleifend tempus ligula, ut placerat dui ullamcorper eget. </p>
    <b-button :to="{name: 'game_1',params: {}}" > ¡¡ Juega !! </b-button>
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
