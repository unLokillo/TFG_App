(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-f3097bd6"],{"2f4f":function(t,e,s){},"528e":function(t,e,s){"use strict";s.r(e);var o=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"all-neologismes-card"},[s("div",{staticClass:"close-modal"},[s("a",{on:{click:function(e){return t.$router.go(-1)}}},[s("font-awesome-icon",{staticStyle:{"font-size":"140%"},attrs:{icon:"times"}})],1)]),t._m(0),s("div",{staticClass:"neologisme-cards"},t._l(t.neologismes,(function(e,o){return s("div",{key:o},[s("b-avatar",{attrs:{src:e.img}}),s("h5",[t._v(t._s(e.neologisme))]),s("div",[s("font-awesome-icon",{attrs:{icon:"heart"}}),t._v(" "+t._s(e.liked)+" ")],1),s("b-button",{staticClass:"bttn-app",attrs:{to:{name:"fv-neologismes",params:{userid:t.$route.params.userid,neoId:e.id}}}},[t._v(" +")])],1)})),0)])},a=[function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"top-all-neologismes"},[s("h5",[t._v(" Neologismos favortios ")])])}],n=s("bc3a"),i=s.n(n),c={created:function(){var t=this;i.a.get("http://localhost:3000/login/1").then((function(e){t.login=e.data,i.a.get("http://localhost:3000/users/"+t.$route.params.userid).then((function(e){i.a.get("http://localhost:3000/neologismes").then((function(s){for(var o=0;o<e.data.fav_neo.length;o++)t.neologismes.push(s.data[e.data.fav_neo[o]-1])}))}))}))},data:function(){return{neologismes:[],login:[]}},methods:{submit:function(t,e,s){var o={};switch(e){case"accepted":o={proposal:!1};break;case"reject":o={rejected:!0,mssg:s};break}i.a.patch("http://localhost:3000/neologismes/"+t,o)}}},l=c,r=(s("ddf6"),s("2877")),u=Object(r["a"])(l,o,a,!1,null,null,null);e["default"]=u.exports},ddf6:function(t,e,s){"use strict";s("2f4f")}}]);
//# sourceMappingURL=chunk-f3097bd6.1897d0bf.js.map