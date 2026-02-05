import { auth } from "@/lib/auth/auth"; // Point to the file we made in Step 1
import { toNextJsHandler } from "better-auth/next-js";

export const { GET, POST } = toNextJsHandler(auth);