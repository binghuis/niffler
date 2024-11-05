import fastify from "fastify";
import router from "./router";
import fastifyPlugin from "fastify-plugin";
import envPlugin from "./plugins/env";
const server = fastify({
  // Logger only for production
  logger: !!(process.env.NODE_ENV !== "development"),
});

server.register(fastifyPlugin(envPlugin));
server.register(router);

export default server;
