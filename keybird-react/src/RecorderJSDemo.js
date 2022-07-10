import './App.css';
import axios from "axios";

let gumStream = null;
let recorder = null;
let audioContext = null;

function RecorderJSDemo() {

    const startRecording = () => {
        let constraints = {
            audio: true,
            video: false
        }

        audioContext = new window.AudioContext();
        console.log("sample rate: " + audioContext.sampleRate);

        navigator.mediaDevices
            .getUserMedia(constraints)
            .then(function (stream) {
                console.log("initializing Recorder.js ...");

                gumStream = stream;

                let input = audioContext.createMediaStreamSource(stream);

                recorder = new window.Recorder(input, {
                    numChannels: 1
                })

                recorder.record();
                console.log("Recording started");
            }).catch(function (err) {
                //enable the record button if getUserMedia() fails
        });

    }

    const stopRecording = () => {
        console.log("stopButton clicked");

        recorder.stop(); //stop microphone access
        gumStream.getAudioTracks()[0].stop();

        recorder.exportWAV(onStop);
    }

    const onStop = (blob) => {
        console.log("uploading...");

        let data = new FormData();

        data.append('text', "this is the transcription of the audio file");
        data.append('wavfile', blob, "recording.wav");

        const config = {
            headers: {'content-type': 'multipart/form-data'}
        }
        axios.post('http://localhost:8080/asr/', data, config);
    }

    return (
        <div>
            <button onClick={startRecording} className='StartRecordButton' type="button">
                <svg width="48" height="48" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 386.972 386.972" xmlSpace="preserve"><path d="M25.99 0v386.972l334.991-193.486L25.99 0zm30 51.972 245.009 141.514L55.99 335V51.972z"/></svg>
            
            </button>
            <button onClick={stopRecording} className='StopRecordButton' type="button">
            <svg width="48" height="48" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 365 365" xmlSpace="preserve"><path d="M74.5 0h73v365h-73zM217.5 0h73v365h-73z"/></svg>
            </button>
            <h4>
                Record Audio
            </h4>

        </div>
    );
}

export default RecorderJSDemo;
