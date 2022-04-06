<template>
    <div class="footer-card">
        <div class="links-menu">
            <router-link class="links" :to="{ name: 'info',params: {} }"> Información </router-link>
            <div></div>
            <router-link class="links" :to="{ name: 'faq',params: {} }"> Preguntas Frecuentes </router-link>
        </div>   
           <p> Pescaneo </p>
    </div>
</template>
<style>
.footer-card{
    display: flex;
    background: var(--third-color);
    border-top: 1px solid var(--border);
    padding: 1% 5% 0 5%;
    justify-content: space-between;
}

.links{
    min-width: 158px;
}

.links-menu{
    width: 20%;
    display: flex;
    justify-content: space-between;
}
</style>