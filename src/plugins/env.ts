import * as dotenv from "dotenv";
import { FastifyPluginAsync } from "fastify";

const configPlugin: FastifyPluginAsync = async (server) => {
  try {
    const envConfig = dotenv.config({ path: [".env.local"] });
    server.decorate("config", envConfig.parsed);
  } catch (err) {
    server.log.error(err);
    throw err;
  }
};

export default configPlugin;
