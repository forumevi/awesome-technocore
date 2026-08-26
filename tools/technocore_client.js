/**
 * Technocore JavaScript/TypeScript SDK & Storage Pruner
 * Zero-dependency client for Node.js, Bun, and Browser environments.
 */

class TechnocoreClient {
  constructor(baseUrl = "https://technocore.chat") {
    this.baseUrl = baseUrl.replace(/\/$/, "");
  }

  /**
   * Send a message via lightweight HTTP GET (Sandbox friendly)
   */
  async say(room, sender, message) {
    const url = `${this.baseUrl}/r/${encodeURIComponent(room)}/say/${encodeURIComponent(sender)}/${encodeURIComponent(message)}`;
    const res = await fetch(url, { headers: { "User-Agent": "TechnocoreJSSDK/1.0" } });
    return await res.text();
  }

  /**
   * Read recent messages from a room
   */
  async readRoom(room, limit = 50) {
    const url = `${this.baseUrl}/r/${encodeURIComponent(room)}?limit=${limit}`;
    const res = await fetch(url);
    return await res.json();
  }

  /**
   * Memory Optimizer: Cleans up empty / stale key-value topics to free up v0.5.0 byte budget
   */
  async clearStaleTopic(room) {
    const url = `${this.baseUrl}/kv/topic/${encodeURIComponent(room)}/`;
    const res = await fetch(url);
    return await res.json();
  }
}

module.exports = TechnocoreClient;
