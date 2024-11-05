import { FastifyInstance } from "fastify";
declare module "fastify" {
  interface FastifyInstance {
    config: {} & FastifyInstance["config"];
  }
}
