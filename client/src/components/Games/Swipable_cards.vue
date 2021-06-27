<template>
<div>
  <Header/>
  <section class="container">
    <div
      v-if="current"
      class="fixed fixed--center"
      style="z-index: 3"
      :class="{ 'transition': isVisible }">
      <Vue2InteractDraggable
        v-if="isVisible"
        :interact-out-of-sight-x-coordinate="500"
        :interact-max-rotation="15"
        :interact-x-threshold="200"
        :interact-y-threshold="200"
        :interact-event-bus-events="interactEventBus"
        interact-block-drag-down
        @draggedRight="emitAndNext('match',current.id)"
        @draggedLeft="emitAndNext('reject',current.id)"
        style="display: flex;justify-content: center"
        class="rounded-borders card card--one">
        <div >
        <div class="image_container">
          <img
            style="width:40%"
            v-if="current.src!=null"
            :src="require(`../../assets/images/${current.src}`)"
            class="rounded-borders"/>
        </div>
        <div class="info">
          <div class="game-card">
          <h5>Contexto</h5>
            <div v-if="current.descriptions.length>0">
              <p> 1 - {{ current.descriptions[0].value }}</p>
            </div>

            <h5>Fuentes</h5>
            <div v-if="current.sources.length>0">
              <p> 1 - {{ current.sources[0].value }}</p>
            </div>

          </div>
        </div>
          <div class="text">
            <h2>{{current.name}}</h2>
          </div>
          </div>
      </Vue2InteractDraggable>
    </div>
    <div
      v-if="next"
      class="rounded-borders card card--two fixed fixed--center"
      style="z-index: 2">
      <div style="height: 100%">
        <img
          :src="next.src"
          class="rounded-borders"/>
        <div class="text">
            <h2>{{next.name}}, <span>{{next.age}}</span></h2>
          </div>
      </div>
    </div>
    <div
      v-if="index + 2 < cards.length"
      class="rounded-borders card card--three fixed fixed--center"
      style="z-index: 1">
      <div style="height: 100%">
      </div>
    </div>
    <!--
    <div class="footer fixed">
      <div class="btn btn--decline" @click="reject">
       <font-awesome-icon icon="times"/>
      </div>
      <div class="btn btn--like" @click="match()">
          <font-awesome-icon icon="heart"/>
      </div>
    </div>
    -->
  </section>
 </div> 
</template>
<script>
import axios from 'axios'
import Header from '@/components/Header/Header.vue'
import { Vue2InteractDraggable, InteractEventBus } from 'vue2-interact'
const EVENTS = {
  MATCH: 'match',
  REJECT: 'reject'
}
export default {
  components: 
  { Vue2InteractDraggable,
  Header },
    created(){
      var nData = [];
      var card = [];
        axios.get('http://localhost:3000/login/1')
        .then(response_l => {
        axios.get('http://localhost:3000/users/' + response_l.data.user_id)
        .then(response_u => {
          console.log(response_u.data)
          this.userData = response_u.data;
        axios.get('http://localhost:3000/neologismes')
        .then(response => {
            //this.name = response.data[0].name;
          for (let i = 0; i < response.data.length; i++) {
          if(!response_u.data.fav_neo.includes(response.data[i].id)){
          card.push({
            id: response.data[i].id,
            src: response.data[i].img,
            name: response.data[i].neologisme,
            descriptions: response.data[i].descriptions,
            sources: response.data[i].sources
          });
        }
      }
          this.nData = response.data; 
        })
        })
        })
      this.cards = card;
      this.neoData = nData;   
    },
  data() {
    return {
      neoData: [],
      isVisible: true,
      index: 0,
      userData: [],
      interactEventBus: {
        draggedRight: EVENTS.MATCH,
        draggedLeft: EVENTS.REJECT,
      },
      cards: []
    }
  },
  computed: {
    current() {
      return this.cards[this.index]
    },
    next() {
      return this.cards[this.index + 1]
    }
  },
  methods: {
    match(id) {
      InteractEventBus.$emit(EVENTS.MATCH);
      axios.patch('http://localhost:3000/neologismes/' + id,{liked: this.nData.liked+1}).then(response_l => {
      });
    },
    reject() {
      InteractEventBus.$emit(EVENTS.REJECT)
    },
    emitAndNext(event,id) {
      if(event.localeCompare('match')==0){
         axios.patch('http://localhost:3000/neologismes/' + id,{liked: this.nData.liked+1}).then(response_l => {
      });
      this.userData.fav_neo.push(id);
       axios.patch('http://localhost:3000/users/' + this.userData.id,{fav_neo: this.userData.fav_neo}).then(response_l => {
      });
      }
      this.$emit(event, this.index)
      setTimeout(() => this.isVisible = false, 200)
      setTimeout(() => {
        this.index++
        this.isVisible = true
      }, 200)
    }
  }
}
</script>

<style lang="scss" scoped>

.container {
  background: #eceff1;
  width: 100%;
  height: 52rem;
}

.footer {
  width: 77vw;
  bottom: 10%;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  padding-bottom: 30px;
  justify-content: space-around;
  align-items: center;
}
.btn {
  position: relative;
  width: 50px;
  height: 50px;
  padding: .2rem;
  border-radius: 50%;
  background-color: white;
  box-shadow: 0 6px 6px -3px rgba(0,0,0,0.02), 0 10px 14px 1px rgba(0,0,0,0.02), 0 4px 18px 3px rgba(0,0,0,0.02);
  cursor: pointer;
  transition: all .3s ease;
  user-select: none;
  -webkit-tap-highlight-color:transparent;
  &:active {
    transform: translateY(4px);
  }
  i {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    &::before {
      content: '';
    }
  }
  &--like {
    background-color: red;
    padding: .75rem;
    color: white;
    box-shadow: 0 10px 13px -6px rgba(0,0,0,.2), 0 20px 31px 3px rgba(0,0,0,.14), 0 8px 38px 7px rgba(0,0,0,.12);
    i {
      font-size: 32px;
    }
  }
  &--decline {
        padding: .75rem;
    color: red;
  }
}
.flex {
  display: flex;
  &--center {
    align-items: center;
    justify-content: center;
  }
}
.fixed {
  position: fixed;
  &--center {
    left: 50%;
    top: 55%;
    transform: translate(-50%, -55%);
  }
}
.rounded-borders {
  border-radius: 12px;
}
.card {
  width: 40vw;
  height: 75vh;
  color: white;
  img {
    object-fit: cover;
    display: block;
    width: 100%;
    height: 100%;
  }
  &--one {
    box-shadow: 0 1px 3px rgba(0,0,0,.2), 0 1px 1px rgba(0,0,0,.14), 0 2px 1px -1px rgba(0,0,0,.12);
  }
  &--two {
    transform: translate(-48%, -48%);
    box-shadow: 0 6px 6px -3px rgba(0,0,0,.2), 0 10px 14px 1px rgba(0,0,0,.14), 0 4px 18px 3px rgba(0,0,0,.12);
  }
  &--three {
    background: rgba(black, .8);
    transform: translate(-46%, -46%);
    box-shadow: 0 10px 13px -6px rgba(0,0,0,.2), 0 20px 31px 3px rgba(0,0,0,.14), 0 8px 38px 7px rgba(0,0,0,.12);
  }
  .text {
    position: absolute;
    bottom: 0;
    width: 100%;
    background:black;
    background:rgba(0,0,0,0.5);
    border-bottom-right-radius: 12px;
    border-bottom-left-radius: 12px;
    text-indent: 20px;
    span {
      font-weight: normal;
    }
  }
}

.image_container{
  width: 80%; 
  margin: 10px auto;
  display: flex;
  justify-content: center;
  border-bottom: 1px solid var(--border);
}

.transition {
  animation: appear 200ms ease-in;
}
@keyframes appear {
  from {
    transform: translate(-48%, -48%);
  }
  to {
    transform: translate(-50%, -50%);
  }
}

.info{
    width: 80%;
    margin-bottom: 2%;
    margin: 10px auto;
    color: black  ;
  .game-card{

    text-align: left;
    border-left: 10px solid var(--border-left);
    padding: 0 10%;
    font-size: 14px;
    overflow: scroll;
  }
}
</style>