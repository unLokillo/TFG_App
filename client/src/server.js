import { Server, Model } from "miragejs";

export function makeServer({ environment = "development" } = {}) {
  let server = new Server({
    environment,

    models: {
      user: Model,
      neologismo: Model
    },

    seeds(server) {
      server.db.loadData({
        users: [
          { id: 1,
            nickname: "admin",
            surname: "admin",
            email: "email@email.com",
            date: "2021-06-02",
            gender: "No Binary",
            password: "password",
            school: "ETSIINF",
            mother_tonge: "Español",
            image: "default_profile.png",
            position: 0,
            proposals: [],
            accepted_neo: [],
            fav_neo: [],
            points: 2000,
            admin: true,
            linguist: false
          },
          { id: 2,
            nickname: "Rcbjo",
            name: "Raul",
            surname: "Carbajosa Gonzalez",
            email: "raul.carbajosa.gonzalez@gmail.com",
            date: "2000-10-12",
            gender: "Masculino",
            password: "RAulcb1",
            school: "ETSIINF",
            mother_tonge: "Español",
            image: "default_profile.png",
            points: 0,
            position: 4,
            proposals: [],
            accepted_neo: [
              3
            ],
            fav_neo: [
              1
            ],
            admin: false,
            linguist: false
        }
        ],
        neologismes: [
          {
            neologismo: "Hackear",
            descriptions: [
              {
                id: 1,
                value: "Se hackea una cuenta en las redes sociales o un correo electrónico"
              },
              {
                id: 2,
                value: "Robar la identidad del hackeado, es decir, para hacerse pasar por él."
              },
              {
                id: 3,
                value: "Para vigilar al hackeado y así conocer sus movimientos y rutinas para cometer delitos."
              }
            ],
            sources: [
              {
                id: 1,
                value: "https://www.argentina.gob.ar/justicia/convosenlaweb/situaciones/me-hackearon-la-cuenta-de-Facebook-que-hago"
              }
            ],
            img: "neologismos.jpg",
            liked: null,
            proposal: false,
            position: 1,
            mssg: "",
            user: [
              {
                user_id: 2,
                user: "Martin martin",
                date: "30/10/1998",
                rejected: false
              }
            ],
            id: 1
          },
          {
            neologismo: "Feature",
            descriptions: [
              {
                id: 1,
                value: "El Desarrollo de Software Orientado a Features (FOSD)..."
              },
              {
                id: 2,
                value: "Una  característica  (feature)  es  una  unidadfuncional  de  un  sistema  de  software "
              }
            ],
            sources: [
              {
                id: 2,
                value: "ANÁLISIS  DE  DESARROLLO  DE  SOFTWARE  ORIENTADO  A FEATURE - LÍNEA DE PRODUCTO DE SOFTWARE PARA APLICACIONES DE TVDI"
              }
            ],
            img: "neologismos.jpg",
            liked: 6,
            proposal: false,
            position: 2,
            user: [
              {
                user_id: 2,
                user: "Raul Carbajosa",
                date: "02/06/2021",
                rejected: false,
                mssg: ""
              }
            ],
            id: 2
          },
          {
            neologismo: "Prueba 3",
            descriptions: [
              {
                id: 1,
                value: "Prueba 3"
              }
            ],
            sources: [
              {
                id: 1,
                value: "Prueba 3"
              }
            ],
            img: "neologismos.jpg",
            liked: 0,
            proposal: false,
            position: 9,
            user: [
              {
                user_id: 2,
                user: "Rcbjo",
                date: "14/05/2021",
                rejected: false,
                mssg: ""
              }
            ],
            id: 3
          }
        ]
      });
    },

    routes() {
      //this.namespace = "api";
      this.timing = 750;

      this.get("/users", ({ db }) => {
        return db.users;
      });

      this.patch("/users/:id", (schema, request) => {
        let todo = JSON.parse(request.requestBody).data;

        return schema.db.todos.update(todo.id, todo);
      });

      this.get("/neologismes", ({ db }) => {
        return db.neologismes;
      });

      this.post("/todos", (schema, request) => {
        let todo = JSON.parse(request.requestBody).data;

        return schema.db.todos.insert(todo);
      });

      this.delete("/todos/:id", (schema, request) => {
        return schema.db.todos.remove(request.params.id);
      });
    }
  });

  window.server = server;

  return server;
}