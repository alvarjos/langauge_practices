const axios = require('axios');
const fs = require('fs');
const NodeID3 = require('node-id3');
const path = require('path');
const { fileURLToPath } = require('url');

// https://open.spotify.com/episode/1FcKD8YPlhTRDnLQqVPW7h?si=38979de7070b4efb
// Define the podcast URL and the local file path
const podcastUrl = "https://www.byuradio.org/8746b541-952c-4cd1-895d-c149c322461b?utm_source=byub&utm_medium=share&utm_campaign=share_2024&utm_content=episode";
const localFilePath = path.join(__dirname, "downloaded-podcast.mp3");

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

  async function processPodcast() {
    try {
        console.log("Downloading podcast...")
        await downloadPodcast(podcastUrl, localFilePath)

        console.log(`Podcast processed successfully. File saved at: ${localFilePath}`)
    }
    catch(err) {
        console.log("An error occured: ", err)
    }
  }

  processPodcast();