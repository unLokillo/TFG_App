<template v-if="appear">
  <div>
    <Header />
    <section class="container">
      <div
        class="fixed fixed--center"
        style="z-index: 3"
        :class="{ transition: isVisible }"
      >
        <Vue2InteractDraggable
          v-if="isVisible & !finished"
          :interact-out-of-sight-x-coordinate="500"
          :interact-max-rotation="15"
          :interact-x-threshold="200"
          :interact-y-threshold="200"
          :interact-event-bus-events="interactEventBus"
          interact-block-drag-down
          @draggedRight="emitAndNext('match', current.id)"
          @draggedLeft="emitAndNext('reject', current.id)"
          style="display: flex; justify-content: center; margin-top:-70px; background-color: lightblue;"
          class="rounded-borders card card--one"
        >
          <div>
            <!--<div class="image_container">
              <img
                style="width: 40%"
                v-if="current.src != null"
                :src="require(`../../assets/images/${current.src}`)"
                class="rounded-borders"
              />
            </div>-->
            <div class="image_container" style="color: black; margin-bottom:70px" v-if="appear & !finished"><h1>{{current.name_eng}}</h1></div>
            <div class="info">
              <div class="game-card" v-if="appear">
                <h5>Context</h5>
                <div v-for="(value, index) in current.descriptions" :key="index" >
                  <p>{{index+1}} - {{ value[0] }}</p>
                </div>

                <h5>Sources</h5>
                <div>
                <div v-for="(value, index) in current.sources" :key="index">
                  <p>{{index+1}} - {{ value[0] }}</p>
                </div>
                </div>
              </div>
            </div>
            <div class="text" v-if="appear">
              <h2>{{ current.name }}</h2>
            </div>
          </div>
        </Vue2InteractDraggable>
      </div>
      <div
        v-if="next"
        class="rounded-borders card card--two fixed fixed--center"
        style="z-index: 2; margin-top:-30px; background-color: lightblue"
      >
        <div style="height: 100%">
          <!-- <img :src="next.src" class="rounded-borders" /> -->
          <div class="image_container" style="color: black; margin-bottom:70px; margin-top: 120px"><h1>{{next.name_eng}}</h1></div>
          <div class="info">
              <div class="game-card" v-if="appear">
                <h5>Context</h5>
                <div v-for="(value, index2) in next.descriptions" :key="index2" >
                  <p>{{index2+1}} - {{ value[0] }}</p>
                </div>

                <h5>Sources</h5>
                <div>
                <div v-for="(value, index3) in next.sources" :key="index3">
                  <p>{{index3+1}} - {{ value[0] }}</p>
                </div>
                </div>
              </div>
          </div>
          <div class="text">
            <h2>
              {{ next.name_eng }}
            </h2>
          </div>
        </div>
      </div>
      <div
        v-if="index + 2 < cards.length"
        class="rounded-borders card card--three fixed fixed--center"
        style="z-index: 1; margin-top: -30px"
      >
        <div style="height: 100%"></div>
      </div>
      <div v-if="finished" style="justify-content: space-around; align-items: center; padding:20%;">
        <h1>GAME FINISHED, CONGRATULATIONS!</h1>
        <br>
        <b-button
        style="width:200px; background-color:var(--buttons); color: white !important; border: none; padding:12px; text-decoration: none;"
        class="rounded-borders"
        :to="`/`"
        @click="get_achievement"
        >
          Go home
        </b-button>
      </div>
      <div style="display: flex; padding-top:20%" v-if="!finished">
        <font-awesome-icon
          style="color: red; font-size: 50px; padding-left:10%"
          icon="circle-xmark"
        />
        <font-awesome-icon
          style="color: #50cd5d; font-size: 50px; padding-left:70%"
          icon="heart"
        />
      </div>
    </section>
  </div>
</template>
<script>
import axios from "axios";
import Header from "@/components/Header/Header.vue";
import { Vue2InteractDraggable, InteractEventBus } from "vue2-interact";
const EVENTS = {
  MATCH: "match",
  REJECT: "reject",
};
export default {
  components: { Vue2InteractDraggable, Header },
  async created() {
    var nData = [];
    var card = [];
    await axios.get("http://127.0.0.1:5000/login", { withCredentials: true })
    .then(res => {
      this.userData = res.data;
    });
    await axios.get("http://127.0.0.1:5000/users/"+ this.userData.user_id + "/favs", { withCredentials: true })
    .then(res => {
      this.favs = res.data;
    });
    axios.get("http://127.0.0.1:5000/neologismes", { withCredentials: true })
    .then(res => {
      for(let i = 0; i < res.data.length; i++) {
        if(!this.isfav(res.data[i].id)&&res.data[i].state=='aceptado'){
          card.push({
                  id: res.data[i].id,
                  name: res.data[i].neologismo,
                  name_eng: res.data[i].name_eng,
                  descriptions: res.data[i].descriptions,
                  sources: res.data[i].sources,
                });
        }
      }
      this.cards = card;
      this.nData = res.data;
    });
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
      cards: [],
      favs: [],
    };
  },
  computed: {
    current() {
      return this.cards[this.index];
    },
    next() {
      return this.cards[this.index + 1];
    },
    appear(){
      return this.cards.length>0
    },
    finished(){
      return this.index>=this.cards.length
    }
  },
  methods: {
    get_achievement(){
      var formData = new FormData();
      formData.append("achiev", 5);
      axios.post("http://127.0.0.1:5000/badges", formData, { withCredentials: true })
      .then(res => {
        if(res.status == 201){
          this.flashMessage.show({
                  status: "success",
                  title: "You have earned a new badge!",
                  message: "Go to your badges section to check it out",
                  time: 5000,
                  position: 'left top',
                  contentClass: 'flashnotif'
                });
        }
      });
    },
    isfav(id){
      var is = false;
      for(var i = 0; i < this.favs.length; i++){
        if(this.favs[i].id == id){
          is = true;
          break;
        }
      }
      return is;
    },
    reject() {
      InteractEventBus.$emit(EVENTS.REJECT);
    },
    emitAndNext(event, id) {
      if (event.localeCompare("match") == 0) {
        axios
        .get("http://127.0.0.1:5000/login", { withCredentials: true })
        .then((res) => {
          if (res.status != 200)
            this.$router.push("/login");
        });
        axios.post(
            "http://127.0.0.1:5000/neologismes/" +
              id + "/likes", "carga",
            { withCredentials: true }
          );
      }
      this.$emit(event, this.index);
      setTimeout(() => (this.isVisible = false), 200);
      setTimeout(() => {
        this.index++;
        this.isVisible = true;
      }, 200);
    },
  },
};
</script>

<style lang="scss" scoped>
.container {
  background: #eceff1;
  width: 100%;
  height: 37.5rem;/*52rem;*/
  color:#50cd5d
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
  padding: 0.2rem;
  border-radius: 50%;
  background-color: white;
  box-shadow: 0 6px 6px -3px rgba(0, 0, 0, 0.02),
    0 10px 14px 1px rgba(0, 0, 0, 0.02), 0 4px 18px 3px rgba(0, 0, 0, 0.02);
  cursor: pointer;
  transition: all 0.3s ease;
  user-select: none;
  -webkit-tap-highlight-color: transparent;
  &:active {
    transform: translateY(4px);
  }
  i {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    &::before {
      content: "";
    }
  }
  &--like {
    background-color: red;
    padding: 0.75rem;
    color: white;
    box-shadow: 0 10px 13px -6px rgba(0, 0, 0, 0.2),
      0 20px 31px 3px rgba(0, 0, 0, 0.14), 0 8px 38px 7px rgba(0, 0, 0, 0.12);
    i {
      font-size: 32px;
    }
  }
  &--decline {
    padding: 0.75rem;
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
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2), 0 1px 1px rgba(0, 0, 0, 0.14),
      0 2px 1px -1px rgba(0, 0, 0, 0.12);
  }
  &--two {
    transform: translate(-48%, -48%);
    box-shadow: 0 6px 6px -3px rgba(0, 0, 0, 0.2),
      0 10px 14px 1px rgba(0, 0, 0, 0.14), 0 4px 18px 3px rgba(0, 0, 0, 0.12);
  }
  &--three {
    background: rgba(black, 0.8);
    transform: translate(-46%, -46%);
    box-shadow: 0 10px 13px -6px rgba(0, 0, 0, 0.2),
      0 20px 31px 3px rgba(0, 0, 0, 0.14), 0 8px 38px 7px rgba(0, 0, 0, 0.12);
  }
  .text {
    position: absolute;
    bottom: 0;
    width: 100%;
    background: black;
    background: rgba(0, 0, 0, 0.5);
    border-bottom-right-radius: 12px;
    border-bottom-left-radius: 12px;
    text-indent: 20px;
    span {
      font-weight: normal;
    }
  }
}

.image_container {
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

.info {
  width: 80%;
  margin-bottom: 2%;
  margin: 10px auto;
  color: black;
  .game-card {
    text-align: left;
    border-left: 10px solid var(--border-left);
    padding: 0 10%;
    font-size: 14px;
    // overflow: scroll;
  }
}
.flashnotif {
  font-size: 20px;
}
</style>