const fs = require("fs");
const path = require("path");

const [assignmentId, displayName, filename, type] = process.argv.slice(2);

if (!assignmentId || !displayName || !filename || !type) {
  console.error(
    'Usage: node add-attachment.js <assignment-id> "<display-name>" <filename> <type>',
  );
  process.exit(1);
}

const repoRoot = path.resolve(__dirname, "../../../..");
const configPath = path.join(repoRoot, "config.json");
const filePath = path.join(repoRoot, "assignments", assignmentId, filename);

if (!fs.existsSync(filePath)) {
  console.error(`Error: File not found: assignments/${assignmentId}/${filename}`);
  process.exit(1);
}

const config = JSON.parse(fs.readFileSync(configPath, "utf8"));
const assignment = config.assignments.find((item) => item.id === assignmentId);

if (!assignment) {
  console.error(`Error: Assignment "${assignmentId}" not found in config.json`);
  process.exit(1);
}

if (!assignment.attachments) {
  assignment.attachments = [];
}

if (assignment.attachments.some((item) => item.file === filename)) {
  console.log(`Skipped: "${filename}" is already attached to "${assignmentId}"`);
  process.exit(0);
}

assignment.attachments.push({ name: displayName, file: filename, type });
fs.writeFileSync(configPath, JSON.stringify(config, null, 2) + "\n");
console.log(`Added "${displayName}" (${filename}) to assignment "${assignmentId}"`);