import axios from "axios";
import { FastifyInstance, FastifyRequest, FastifyReply } from "fastify";

export default async function xCtrl(fastify: FastifyInstance) {
  fastify.get("/", async (_request: FastifyRequest, reply: FastifyReply) => {
    try {
      const ret = await axios.get(
        "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",
        {
          headers: {
            "X-CMC_PRO_API_KEY": fastify.config.CMC_API_KEY,
          },
        }
      );

      reply.send(ret.data);
    } catch (error) {
      console.error("Error details:", error);
      reply.status(500).send({ error: "Internal Server Error" });
    }
  });
}
