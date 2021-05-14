<template>
  <div>
    <div v-b-toggle.sidebar-no-header class="hamburguer-button"> <font-awesome-icon icon="bars"/>Menu</div>
    <b-sidebar id="sidebar-no-header" aria-labelledby="sidebar-no-header-title" no-header shadow>
      <template #default="{ hide }">
        <div>
          <div class="sidemenu-top">
            <h4 id="sidebar-no-header-title">Menu</h4>
            <div style="cursor:pointer;" block @click="hide"><font-awesome-icon style="font-size: 200%;" icon="bars"/></div>
          </div>
          <div class="all-sidebar-buttons">
                <div class="sidebar-button" v-for="(btn, index) in buttons" :key="index">
                  <font-awesome-icon style="font-size: 120%; !important" :icon="btn.icon" /> {{ btn.caption }}
                </div>
          <router-link :to="{ name: 'games',params: {} }" class="sidebar-button" style="  border-left: 10px solid red !important;" tag="div">
              <font-awesome-icon style="font-size: 120%; !important" :icon="bars" /> AJUGAR
          </router-link>
            <div class="sidebar-button" style="  border-left: 10px solid red !important;" v-if="logged">
              <font-awesome-icon style="font-size: 120%; !important" :icon="bars" /> Salir
          </div>
          
          </div>

        </div>
      </template>
    </b-sidebar>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        myToggle: false,
        buttons: [
          { icon: 'gamepad', caption: 'Juego', state: true },
          { icon: 'gamepad', caption: 'Toggle 2', state: false },
          { icon: 'gamepad', caption: 'Toggle 3', state: true },
          { icon: 'gamepad', caption: 'Toggle 4', state: false }
        ],
        logged: false
      }
    },
    computed: {
      btnStates() {
        return this.buttons.map(btn => btn.state)
      }
    }
  }
</script>

<style>

.option-button{
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: left;
}

.hamburguer-button{
  height: 100%;
  display: flex;
  max-width: 150px;
  justify-content:space-evenly;
  align-items: center;
  border-right: 1px solid var(--border);
}

.all-sidebar-buttons{
    display: flex;
    flex-direction: column;
}

.sidebar-button{
  padding: 8%;
  display: flex;
  font-size: 130%;
  justify-content: center;
  align-items: center;
  justify-content: space-evenly;
  border-bottom: 1px solid var(--border);
  border-left: 10px solid var(--border-left) ;
  cursor: pointer;
}

.sidemenu-top{
  border-bottom: 1px solid var(--border);
  padding: 3% 0 3% 0;
  display: flex;
  justify-content: center;
  align-items: center;
  justify-content: space-around;
}
</style>