<template>
    <div class="ranking-card">
    <div class="ranking-title">
    <h3> Ranking </h3>
    </div>
     <b-table small :fields="labels" :items="items" responsive="sm">
        <template #cell(img)="data">
         <b-avatar :src="data.item.img"></b-avatar>   
    </template>
    </b-table>
    <b-button class="more-bttn">Ver mas</b-button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            labels: [,
            { key: 'img', label: 'Full Name' },
            'position','username', 'points'],
            items: [
                {img: 'https://picsum.photos/300/150/?image=41',position: 1,username: 'User1',points: '2000'},
                {img: 'https://picsum.photos/300/150/?image=40',position: 2,username: 'User2',points: '1899'}
            ]
        }
    }
}
</script>


<style>
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
</style>