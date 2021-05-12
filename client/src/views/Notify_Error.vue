<template>
    <div class="reject-body">
              <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
        <h2> Notificar Error </h2>
        <p> Porfavor escriba a continuación la razón del error, intente entrar en mayor detalle posible</p>
        <b-form-textarea placeholder="Introduce la información del rechazo" rows="5" max-rows="150" class="reject-info"></b-form-textarea>
        <!--<p>Adjunte una imagen si lo cree necesario</p>
        <b-form-file v-model="img" :state="Boolean(img)" placeholder="Choose a file or drop it here..." drop-placeholder="Drop file here..." plain></b-form-file> -->
    <div class="mt-3">Selected file: {{ img ? img.name : '' }}</div>
        <b-button style="background-color: var(--success) !important"> Aceptar </b-button>
    </div>
</template>

<script>
export default {
    data(){
        return{}
    }
}
</script>

<style scoped>
h2{
    border-bottom: 1px solid var(--fail);
    padding-bottom: 2%;
}

.reject-body{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 3%;
}

.reject-info{
    width: 100% ;
    min-height: 50%;
    border: 2px solid var(--fail);
}

</style>
