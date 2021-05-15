<template>
    <div class="bages-section">
        <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
        <div class="top-badges_menu-section">
        <h3>Logros</h3>
        </div>
        <div class="main-section">
             <div v-for="(value,index) in badges" :key="index"  class="neologismes-badges_menu" >
             <b-img src="https://picsum.photos/600/300/?image=20" v-bind="mainProps" rounded alt="Rounded image"></b-img>
             <p>AJAJAJAJ ASI ES DOÑA</p>
             <base-progress color="blue" percentage="50" class="mx-2 mb-2"
        ></base-progress>
             </div>
        </div>
    <!--
        <div class="main-section">
            <div v-for="(value,index) in badges" :key="index"  class="neologismes-badges_menu" >
                <div style="overflow: scroll;">
                <b-card img-src="https://picsum.photos/600/300/?image=25" img-alt="Image" img-top style="max-width: 20rem; max-height: 20rem;" class="mb-2">
                <h6 style="border-bottom: 1px solid var(--border); padding-bottom: 1px;">{{ value.name_badge }}</h6>
                <b-card-text style="font-size: 13px;">
                    {{ value.text }}
                </b-card-text>
                <div style="border-top: 1px solid var(--border);" v-if="value.completed">
                    mira me cago en dios
                </div>
                </b-card>
                </div>
            </div>
        </div>
        -->
    </div>
</template>

<script>
import BaseProgress from "@/components/User_View/BaseProgress";

export default {
  name: 'View-User',
  components: {
      BaseProgress
    },
    data(){
        return{
            mainProps: {width: 75, height: 75, class: 'm1' },
            user_id: '123456789',
            badges: [
                {id_badge: '123456',text: "Logueate 3 veces en la apliacion",completed: false,name_badge: 'Badge_1',completed_date: 'XX/XX/XXXX',completion_percentage: 50},
                {id_badge: '123456',text: "Logueate 5 veces en la apliacion",completed: true,name_badge: 'Badge_2',completed_date: '30/10/1998',completion_percentage: 50},
                {id_badge: '123456',text: "Marca un neologismo como megusta",completed: false,name_badge: 'Badge_3',completed_date: 'XX/XX/XXXX',completion_percentage: 50},
                {id_badge: '123456',text: "Marca dos neologismo como megusta",completed: true,name_badge: 'Badge_4',completed_date: 'XX/XX/XXXX',completion_percentage: 50}
            ],
            v_a: 33.333333333,
            m_a: 50.0,
        }
    }
}
</script>

<style>
.top-badges_menu-section{
    display: flex;
    justify-content: space-around;
    padding: 2%;
    border-bottom: 1px solid var(--border);

}

.neologismes-badges_menu{
display: flex;
flex-direction: column;
align-items: center;
border: 1px solid var(--border);
margin: 2%;
}

.neologismes-badges_menu > div{
    margin: 3%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    }

.badge-card-unfinished{
    opacity: 0.5;
}
</style>