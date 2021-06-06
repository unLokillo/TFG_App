<template>
    <div class="card-body">
        <div class="card-neo-header">
            <h2>{{ neologismeData.neologisme }}</h2>
            <div class="neo-likes" ><font-awesome-icon icon="heart"/> {{ this.neologismeData.liked }}</div> 
        </div>
        <div v-for="(value,index) in neologismeData.descriptions" :key="index" >
            <div v-if="index<3" class="descriptions">{{ index }}.- {{ value.value }}</div>
        </div>
        <div class="user-tag">
            <div>Creado por: {{ neologismeData.user[0].user }} </div> 
            <div>{{ neologismeData.user[0].date }} </div>
        </div>
        <router-link :to="`/fav-neo/${neologismeData.id}`" tag="b-button" style="width: 100%;"> Ver más </router-link>
       
    </div>

</template>

<script>
export default {    
props: {
    neologismeData: Object,
    required: true
  },
watch: {
    $route: {
      immediate: true,
      handler: function(newVal, oldVal) {
        this.showModal = newVal.meta && newVal.meta.showModal;
      }
    }
  },data() {    
        return {
            showModal: false,
            neo_id: '',
            name: '',
            creator:'',
            date: '',
            likes: '',
            descriptions: '',
        };
    },
}
</script>


<style lang="scss" scoped>
.descriptions{
    padding: 3%;
    padding-left: 10%;
    text-align: left;
}
.card-body{
    background-color: var(--third-color);
    max-width: 350px;
}
.card-neo-header{
    display:flex;
    justify-content: space-between;
    align-items: center;
}
.user-tag{
    display:flex;
    flex-direction: column;
    padding-bottom: 5%;
    color: grey;
    font-size: 14px; 
}

</style>