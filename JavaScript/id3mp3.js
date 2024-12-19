// To work with a podcast hosted online via a real URL, you’ll first need to download the MP3 file locally, manipulate its ID3 tags, and then optionally re-upload it. Here's how you can modify the code to handle a real podcast link:

// ### Steps:

// 1. **Download the MP3 File**  
//    Use a library like `axios` or `node-fetch` to fetch the MP3 file from the URL and save it locally.

// 2. **Add Chapters to the Local File**  
//    After downloading the file, use the `node-id3` library as before to modify the ID3 tags.

// 3. **Re-upload the Modified MP3 (Optional)**  
//    If the podcast is hosted online, you may need to upload the modified file back to your hosting service.


const axios = require('axios');
const fs = require('fs');
const NodeID3 = require('node-id3');
const path = require('path');
const mm = requre('music-metadata');
const fs = require('fs')

// Define the podcast URL and the local file path
const podcastUrl = "https://open.spotify.com/episode/1FcKD8YPlhTRDnLQqVPW7h?si=38979de7070b4efb";
const localFilePath = path.join(__dirname, "downloaded-podcast.mp3");


async function getDuration(localFilePath) {
    const metadata = await mm.parseFile(localFilePath)
    const podcastDuration = metadata.format.duration * 1000; // convert to milliseconds
    return podcastDuration
}

getDuration('downloaded-podcast.mp3').then((duration) => {
    console.log(`Podcast Duration: ${duration} ms`)
})

// Define your chapters .. GET ACTUAL TIMES IN MILLISECONDS FOR THE GAME
const chapters = [
  { startTime: 0, endTime: 4860000, title: "BYU vs Arizona State: Pregame" },
  { startTime: 1, endTime: 2, title: "BYU vs Arizona State: 1st Quarter" },
  { startTime: 2, endTime: 3, title: "BYU vs Arizona State: 2nd Quarter" },
  { startTime: 3, endTime: 4, title: "BYU vs Arizona State: 3rd Quarter" },
  { startTime: 4, endTime: 5, title: "BYU vs Arizona State: 4th Quarter" },
  { startTime: 5, endTime: 6, title: "BYU vs Arizona State: Postgame" },
  { startTime: 6, endTime: 7, title: "BYU vs Arizona State: Chase Roberts Postgame Interview" },
  { startTime: 7, endTime: 8, title: "BYU vs Arizona State: Kalani Sitake Postgame Interview" },  
];

// const maxDuration = podcastDuration

// Download the MP3 file
async function downloadPodcast(url, filePath) {
  try {
    const response = await axios({
      url,
      method: 'GET',
      responseType: 'stream',
    });

    // Save the file locally
    const writer = fs.createWriteStream(filePath);
    response.data.pipe(writer);

    return new Promise((resolve, reject) => {
      writer.on('finish', resolve);
      writer.on('error', reject);
    });
  } catch (err) {
    console.error("Error downloading the podcast:", err);
    throw err;
  }
}

// Add chapters to the MP3 file
function addChaptersToPodcast(filePath) {
  const tags = {
    title: "Podcast Episode with Chapters",
    artist: "Your Podcast Name",
    customText: chapters.map((chapter, index) => ({
      description: `Chapter ${index + 1}`,
      value: `Title: ${chapter.title}, Start: ${chapter.startTime}, End: ${chapter.endTime}`,
    })),
  };

  const success = NodeID3.write(tags, filePath);
  if (success) {
    console.log("Chapters added successfully!");
  } else {
    console.error("Error adding chapters to the MP3 file.");
  }
}

// Main function
async function processPodcast() {
  try {
    console.log("Downloading podcast...");
    await downloadPodcast(podcastUrl, localFilePath);

    console.log("Adding chapters...");
    addChaptersToPodcast(localFilePath);

    console.log(`Podcast processed successfully. File saved at: ${localFilePath}`);
  } catch (err) {
    console.error("An error occurred:", err);
  }
}

// Run the main function
processPodcast();


// ### Breakdown of Code:

// 1. **Downloading the Podcast**  
//    The `axios` library fetches the MP3 file and streams it into a local file (`downloaded-podcast.mp3`).

// 2. **Adding Chapters**  
//    After downloading, the `addChaptersToPodcast()` function uses the `node-id3` library to embed metadata into the file.

// 3. **File Handling**  
//    The modified MP3 file is saved locally. You can upload it manually or automate the re-upload process if needed.

// ### To Use This Code:
// - Replace `https://example.com/podcast-episode.mp3` with the URL of your actual podcast.
// - Run the script, and the modified MP3 file with chapters will be saved locally.

// Would you like to explore how to re-upload the file, or need help testing this?


// const chapters = [
//     { startTime: 0, endTime: 60000, title: "Introduction" },
//     { startTime: 60000, endTime: 120000, title: "Main Topic" },
//     { startTime: 120000, endTime: 180000, title: "Conclusion" },
//   ];
  
//   // Dynamically adjust end time to match podcast length
//   const maxDuration = 150000; // Replace with the actual duration in milliseconds
//   const adjustedChapters = chapters.map((chapter) => ({
//     ...chapter,
//     endTime: Math.min(chapter.endTime, maxDuration),
//   }));
  
//   console.log(adjustedChapters);
  