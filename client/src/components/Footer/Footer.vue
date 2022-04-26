<template>
    <div class="footer-card">
        <div class="links-menu">
            <div class="links-menu" v-if="this.$router.currentRoute.path=='/games'">
                <router-link class="links" :to="{ name: 'gamesinfo',params: {} }"> Información </router-link>
                <div></div>
                <router-link class="links" :to="{ name: 'gamesfaq',params: {} }"> Preguntas Frecuentes </router-link>
            </div>
            <div class="links-menu" v-else-if="this.$router.currentRoute.path.includes('view-user')">
                <router-link class="links" :to="{ name: 'userinfo',params: {} }"> Información </router-link>
                
                <router-link class="links" :to="{ name: 'userfaq',params: {} }"> Preguntas Frecuentes </router-link>
            </div>
            <div class="links-menu" v-else >
                <router-link class="links" :to="{ name: 'info',params: {} }"> Información </router-link>
                <div></div>
                <router-link class="links" :to="{ name: 'faq',params: {} }"> Preguntas Frecuentes </router-link>
            </div>
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