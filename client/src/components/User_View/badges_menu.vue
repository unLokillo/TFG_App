<template>
    <div class="bages-section">
        <div class="top-badges_menu-section">
        <h5>Logros</h5>
        <router-link :to="{ name: 'vUser',params: { userid: user_id } }" class="user-bttn" tag="div">
                <font-awesome-icon icon="times"/>
            </router-link>
        </div>

        <div class="main-section">
            <div v-for="(value,index) in badges" :key="index"  class="neologismes-badges_menu" >
                <div style="overflow: scroll;">
                <b-card img-src="https://picsum.photos/600/300/?image=25" img-alt="Image" img-top style="max-width: 20rem; max-height: 20rem;" class="mb-2">
                <h6 style="border-bottom: 1px solid grey; padding-bottom: 1px;">{{ value.name_badge }}</h6>
                <b-card-text style="font-size: 13px;">
                    {{ value.text }}
                </b-card-text>
                <div style="border-top: 1px solid grey;" v-if="value.completed">
                    mira me cago en dios
                </div>
                </b-card>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
  name: 'View-User',
    data(){
        return{
             mainProps: {width: 75, height: 75, class: 'm1' },
            user_id: '123456789',
            badges: [
                {id_badge: '123456',text: "Logueate 3 veces en la apliacion",completed: false,name_badge: 'Badge_1',completed_date: 'XX/XX/XXXX',completion_percentage: 50},
                {id_badge: '123456',text: "Logueate 5 veces en la apliacion",completed: true,name_badge: 'Badge_2',completed_date: '30/10/1998',completion_percentage: 50},
                {id_badge: '123456',text: "Marca un neologismo como megusta",completed: false,name_badge: 'Badge_3',completed_date: 'XX/XX/XXXX',completion_percentage: 50},
                {id_badge: '123456',text: "Marca dos neologismo como megusta",completed: true,name_badge: 'Badge_4',completed_date: 'XX/XX/XXXX',completion_percentage: 50}
            ]
        }
    }
}
</script>

<style>
.top-badges_menu-section{
    display: flex;
    justify-content: space-around;
    padding: 2%;
    border-bottom: 1px solid black;

}

.neologismes-badges_menu{
    display: grid;
    grid-auto-columns: 2fr 2fr 2fr 2fr;
    padding: 3%;
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