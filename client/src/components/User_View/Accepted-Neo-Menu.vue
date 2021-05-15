<template>
    <div class="ranking-card">
    <div class="ranking-title">
    <h3> Neologismos Aceptados </h3>
    </div>
     <div class="neo-card" v-for="(value,index) in items" :key="index" >
         <div v-if="index<5">
         <h5>{{ value.neologismo }}</h5>
            <div>
            <font-awesome-icon icon="heart"/> {{ value.likes }}
            </div>
         <b-button class="bttn-app" :to="{name: 'v-neologisme',params: { userid: $route.params.userid ,neoId: value.id}}"> +</b-button>
        </div>
     </div>
    <router-link :to="{name: 'view-all-neologismes',params: { userid: $route.params.userid }}" class="more-bttn" tag="b-button" >Ver mas</router-link>
    </div>
</template>

<script>
export default {
    watch: {
    $route: {
      immediate: true,
      handler: function(newVal, oldVal) {
        this.showModal = newVal.meta && newVal.meta.showModal;
      }
    }
  },
    data() {
        return {
            showModal: false,
            items: [
                {id: 123456, neologismo: 'Neologismo 1',accepeted: true},
                {id: 123455, neologismo: 'Neologismo 2',accepeted: false},
                {id: 123454, neologismo: 'Neologismo 3',accepeted: false},
                {id: 123453, neologismo: 'Neologismo 4',accepeted: true},
                {id: 123452, neologismo: 'Neologismo 5',accepeted: true},
                {id: 123451, neologismo: 'Neologismo 6',accepeted: true}
            ]
        }
    }
}
</script>


<style lang="scss" scoped>
.ranking-card{
    margin: 40px 10px 40px 10px;
    background-color: var(--third-color);
    
    border: 1px solid var(--border);
}
.ranking-title{
    text-align: left;
    padding-left: 20px;
    color: var(--letter-color);
    background-color: var(--buttons);
}

.more-bttn{
    width: 100%;
    background-color: var(--buttons);
}

.neo-card > div{
    padding: 10px;    
    display: flex;
    justify-content: center;
    align-items: center;
    justify-content: space-evenly;
}

</style>