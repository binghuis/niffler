import { FastifyInstance } from "fastify";
import indexCtrl from "./controller/index.ctrl";
import xCtrl from "./controller/x.ctrl";

export default async function router(fastify: FastifyInstance) {
  fastify.register(indexCtrl, { prefix: "/" });
  fastify.register(xCtrl, { prefix: "/x" });
}
