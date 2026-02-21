export type Config = {
  businessName: string;
  ownerName: string;
  businessHours: string;
  businessAddress: string;
  businessWebsite: string;
  businessPhone: string;
  ignoreGroups: boolean;
  botEnabled: boolean;
  aiEnabled: boolean;
  aiProvider: string;
  aiApiKey: string;
  aiModel: string;
  memoryMaxMessages: number;
};

export function readBool(
  value: string | undefined,
  defaultValue: boolean,
): boolean {
  if (value === undefined) return defaultValue;
  return value !== "false";
}

export const config: Config = {
  businessName: process.env.BUSINESS_NAME || "Our Business",
  ownerName: process.env.OWNER_NAME || "the owner",
  businessHours: process.env.BUSINESS_HOURS || "",
  businessAddress: process.env.BUSINESS_ADDRESS || "",
  businessWebsite: process.env.BUSINESS_WEBSITE || "",
  businessPhone: process.env.BUSINESS_PHONE || "",
  ignoreGroups: readBool(process.env.IGNORE_GROUPS, true),
  botEnabled: true,
  aiEnabled: readBool(process.env.AI_ENABLED, false),
  aiProvider: process.env.AI_PROVIDER || "",
  aiApiKey: process.env.AI_API_KEY || "",
  aiModel: process.env.AI_MODEL || "",
  memoryMaxMessages: Number(process.env.MEMORY_MAX_MESSAGES || 20),
};
