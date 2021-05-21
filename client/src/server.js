import { Server } from "miragejs";

export function makeServer({ environment = "development" } = {}) {
  let server = new Server({
    environment,

    seeds(server) {
      server.db.loadData({
        todos: [
          { name: "Buy groceries", isDone: false },
          { name: "Walk the dog", isDone: false },
          { name: "Do laundry", isDone: false }
        ]
      });
    },

    routes() {
      this.namespace = "api";
      this.timing = 750;

      this.get("/users", ({ db }) => {
        return db.todos;
      });

      this.patch("/users/:id", (schema, request) => {
        let todo = JSON.parse(request.requestBody).data;

        return schema.db.todos.update(todo.id, todo);
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