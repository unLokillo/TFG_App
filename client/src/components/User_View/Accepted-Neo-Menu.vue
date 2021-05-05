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
         <b-button>+</b-button>
        </div>
     </div>
    <router-link :to="`/view-all-neologismes`" class="more-bttn" tag="b-button" >Ver mas</router-link>
     
     <div v-if="showModal" class="modal-route">
        <div class="modal-content">
            <router-view></router-view>
        </div>
    </div>

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
                {neologismo: 'Neologismo 1',accepeted: true},
                {neologismo: 'Neologismo 2',accepeted: false},
                {neologismo: 'Neologismo 3',accepeted: false},
                {neologismo: 'Neologismo 4',accepeted: true},
                {neologismo: 'Neologismo 5',accepeted: true},
                {neologismo: 'Neologismo 6',accepeted: true}
            ]
        }
    }
}
</script>


<style lang="scss" scoped>
.ranking-card{
    margin: 40px 10px 40px 10px;
}
.ranking-title{
    text-align: left;
    padding-left: 20px;
    color: black;
    background-color: lightblue;
}

.more-bttn{
    width: 100%;
    background-color: lightblue !important;
}

.neo-card > div{
    padding: 10px;    
    display: flex;
    justify-content: center;
    align-items: center;
    justify-content: space-evenly;
}

.modal-route {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  background: rgba($color: #000000, $alpha: 0.6);
  
}
.modal-content {
    width: 50%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: white;
  }
</style>