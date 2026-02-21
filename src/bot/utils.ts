import type { Message } from "whatsapp-web.js";
import { config } from "../config";

export async function getNewIssues(message: Message) {
  try {
    const url = `${config.automationApiBaseUrl.replace(/\/+$/, "")}/meroshare/new-issues`;
    const res = await fetch(url, { method: "POST" });

    if (res.status === 409) {
      await message.reply(
        "Another task run is already in progress. Try again later.",
      );
      return true;
    }

    if (!res.ok) {
      await message.reply(
        `Failed to fetch new issues: ${res.status} ${res.statusText}`,
      );
      return true;
    }

    const issues = (await res.json()) as Array<{
      company_name?: string;
      share_type?: string;
      sub_group?: string;
    }>;

    if (!issues || issues.length === 0) {
      await message.reply("No new issues found.");
      return true;
    }

    const lines = issues.map((it, idx) => {
      const name = it.company_name || "(unknown)";
      const type = it.share_type || "(unknown)";
      const subgroup = it.sub_group || "(unknown)";
      return `${idx + 1}. ${name} — ${type} (${subgroup})`;
    });

    // send in one message but guard length
    const reply = `New issues found:\n${lines.join("\n")}`;
    await message.reply(reply);
    return true;
  } catch (err: any) {
    await message.reply(`Error fetching new issues: ${err?.message || err}`);
    return true;
  }
}
