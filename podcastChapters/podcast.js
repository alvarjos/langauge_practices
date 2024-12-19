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

// https://open.spotify.com/episode/1FcKD8YPlhTRDnLQqVPW7h?si=38979de7070b4efb
// Define the podcast URL and the local file path
const podcastUrl = "https://media.byub.org/143db8d9-6005-5ede-9814-831f6f5483d5/BSNS12E267.mp3";
const localFilePath = path.join(__dirname, "downloaded-podcast.mp3");

// Define your chapters
const chapters = [
  { startTime: 0, endTime: 780000, title: "Introduction" },
  { startTime: 780000, endTime: 1920000 , title: "Main Topic" },
  { startTime: 1920000 , endTime: 2997000, title: "Conclusion" },
];

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



function addChaptersToFile(filepath, chapterData) {
    const tags = {
      title: "Podcast Episode",
      customText: chapterData.map((chapter, index) => ({
        description: `Chapter ${index + 1}`,
        value: `Title: ${chapter.title}, Start: ${chapter.startTime}, End: ${chapter.endTime}
        ${chapter.imageUrl ? `, Image: ${chapter.imageUrl}`: ""
        }`
      }))
    }  
  }
  
  function exportChaptersToJson(filepath, chapterData) {
    const jsonFilePath = filePath.replace(".mp3", ".chapters.json")
  
    const jsonContent = {
      version: "1.2",
      chapters: chapterData.map((chapter) => ({
        startTime: timespanToMilliseconds(chapter.startTime),
        endTime: timespanToMilliseconds(chapter.endTime),
        img: chapter.imageUrl || null,
        title: chapter.title,
        toc: true
      }))
    }
    fs.writeFileSync(jsonFilePath, JSON.stringify(jsonContent, null, 2))
    console.log(`Chapters exported to JSON file: ${jsonFilePath}`)
  
  }
  