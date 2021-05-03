<template>
  <div>
    <b-button v-b-toggle.sidebar-no-header class="hamburguer-button">Toggle Sidebar</b-button>
    <b-sidebar id="sidebar-no-header" aria-labelledby="sidebar-no-header-title" no-header shadow>
      <template #default="{ hide }">
        <div>
          <h4 id="sidebar-no-header-title">Custom header sidebar</h4>
          <b-button variant="primary" block @click="hide">Close Sidebar</b-button>
          <div class="sidebar-buttons">
              <b-button-group size=lg vertical block >
                <b-button
                  squared
                  v-for="(btn, idx) in buttons"
                  :key="idx"
                  :pressed.sync="btn.state"
                  variant="primary"
                >
                <font-awesome-icon :icon="btn.icon" /> {{ btn.caption }}
                </b-button>
            </b-button-group>
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
        ]
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
  width: 100%;
}

.sidebar-buttons{
    display: flex;
    flex-direction: column;
}
</style>