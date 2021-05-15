<template>
    <div class="v-ranking-card">
        <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
        <div class="v-ranking-title">
            <h3>Ranking</h3>
        </div>
        <div class="v-ranking-user" v-for="(value,index) in users" :key="index">
            <div class="position-badge" :style="asign_color(value.position)"> <strong> {{ value.position }} </strong></div>
            <div class="avatar-card">
                <b-avatar :src="value.img"></b-avatar> 
                {{value.name}}
            </div>
            <div class="v-ranking-points">
                <font-awesome-icon style="font-size:15px;" icon="trophy"/>
                {{  value.points  }}
            </div>

            <div >
            <b-dropdown right  text="Opciones" class="m-2" v-if="admin">
            <!--<font-awesome-icon style="font-size:30px;" icon="cog"/>-->
                <b-dropdown-item> Eliminar Usuario </b-dropdown-item>
            </b-dropdown>
        </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            admin: true,
            users: [
                {name: "User_1", img: "https://picsum.photos/300/150/?image=41",points: 2100,position: 1},
                {name: "User_2", img: "https://picsum.photos/300/150/?image=40",points: 2002,position: 2},
                {name: "User_3", img: "https://picsum.photos/300/150/?image=39",points: 2000,position: 3},
                {name: "User_4", img: "https://picsum.photos/300/150/?image=38",points: 1999,position: 4},
                {name: "User_5", img: "https://picsum.photos/300/150/?image=37",points: 1999,position: 5},
                {name: "User_6", img: "https://picsum.photos/300/150/?image=36",points: 1999,position: 6},             
                {name: "User_7", img: "https://picsum.photos/300/150/?image=35",points: 1999,position: 7},
                {name: "User_8", img: "https://picsum.photos/300/150/?image=34",points: 1999,position: 8},
                {name: "User_9", img: "https://picsum.photos/300/150/?image=33",points: 1999,position: 9},
            ]
        }
    },
    methods: {
        asign_color: function(pos){
            var style  = {};
            console.log(pos);
            switch(pos){
                default: style.backgroundColor = "var(--buttons)"; break;
                case 1: style.backgroundColor = "var(--gold) "; break;
                case 3: style.backgroundColor = "var(--bronze)"; break;
                case 2: style.backgroundColor = "var(--silver)"; break;
            }
            return style;
        }
    }
}
</script>

<style>
.v-ranking-title{
    border-bottom: 1px solid var(--border);
    margin: 2%;
}

.v-ranking-points{
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.v-ranking-user{
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 3rem;
    border: 1px solid var(--border);
    margin: 2%;
}

.position-badge{
    display: flex;
    align-items: center;
    width: 20%;
    height: 100%;
    justify-content: center;
    color: var(--letter-color);
    font-size: 20px;
}
.avatar-card{
    width: 30%;
    display: flex;
    justify-content: inherit;
    align-items: center;
}

</style>