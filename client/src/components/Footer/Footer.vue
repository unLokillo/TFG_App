<template>
    <div class="footer-card">
        <div class="links-menu">
            <div class="links-menu" v-if="this.$router.currentRoute.path=='/games'">
                <router-link class="links" :to="{ name: 'gamesinfo',params: {} }"> Information </router-link>
                <div></div>
                <router-link class="links" :to="{ name: 'gamesfaq',params: {} }"> FAQ </router-link>
            </div>
            <div class="links-menu" v-else-if="this.$router.currentRoute.path.includes('view-user')">
                <router-link class="links" :to="{ name: 'userinfo',params: {} }"> Information </router-link>
                
                <router-link class="links" :to="{ name: 'userfaq',params: {} }"> FAQ </router-link>
            </div>
            <div class="links-menu" v-else >
                <router-link class="links" :to="{ name: 'info',params: {} }"> Information </router-link>
                <div></div>
                <router-link class="links" :to="{ name: 'faq',params: {} }"> FAQ </router-link>
            </div>
        </div>   
           <p> GreenTerms </p>
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