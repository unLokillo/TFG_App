<template>
    <div class="ranking-card">
    <div class="ranking-title"><h3> Top Neologismos </h3></div>
    <b-table class="ranking-table" small :fields="labels" :items="items" responsive="sm" >
        <template #cell(points)="data">
         <font-awesome-icon icon="heart"/>{{data.item.points}}
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
            'position','neologismo',{ key: 'points', label: 'Me gustas' }],
            items: [
                {position: 1,neologismo: 'Neo1',points: '2000',tdClass: 'nameOfTheClass'},
                {position: 2,neologismo: 'Neo2',points: '1899',tdClass: 'nameOfTheClass'},
                {position: 3,neologismo: 'Neo2',points: '1899',tdClass: 'nameOfTheClass'},
                {position: 4,neologismo: 'Neo2',points: '1899',tdClass: 'nameOfTheClass'},
                {position: 5,neologismo: 'Neo2',points: '1899',tdClass: 'nameOfTheClass'}
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

.ranking-table{
    min-width: 500px;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    border: 1px solid black;
    min-height: 50px;
}

</style>