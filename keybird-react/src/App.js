import logo from './logo.svg';
import './App.css';
import RecorderJSDemo from './RecorderJSDemo';
import AudioUpload from './AudioUpload';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div className='App-wrapper'>
          <div className='Input-wrapper'>
            <div className='UploadAudio'>
              <AudioUpload></AudioUpload>
            </div>
            <hr></hr>
            <div className='RecordAudio'>
              <RecorderJSDemo></RecorderJSDemo>
            </div>
          </div>
          <div className='Output-wrapper'>
            
            <div className='Predictions-wrapper'>
              <div className='Prediction'>
                <div className='Prediction-value'>
                  <div className='Prediction-percentage' id="clicky"></div>
                  <div className='Prediction-svg'>
                    <svg width="48" height="64" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 490" xmlSpace="preserve"><path d="M11.387 490 245 255.832 478.613 490l10.826-10.826-233.63-234.178 233.63-234.185L478.613 0 245 234.161 11.387 0 .561 10.811l233.63 234.185L.561 479.174z"/></svg>
                  </div>
                </div>
                <div className='Prediction-name'>
                  Clicky
                </div>
              </div>
              <div className='Prediction'>
                <div className='Prediction-value'>
                  <div className='Prediction-percentage' id="clacky"></div>
                  <div className='Prediction-svg'>
                    <svg width="48" height="64"  xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" xmlSpace="preserve"><path d="M64 8.9c0-2.786-.794-4.99-2.36-6.55-6.284-6.261-22.806.396-37.62 15.16a20.959 20.959 0 0 0-1.504 1.695 3.468 3.468 0 0 0-.54-.17C17.71 18.04 4.017 20.366.03 36.292a.998.998 0 0 0 1.557 1.053c5.41-3.925 9.751-5.504 13.54-4.923-.261.474-.527.937-.8 1.379a1 1 0 0 0 .143 1.235l1.569 1.564-2.937 2.926a.998.998 0 0 0 0 1.416l9.829 9.797a.997.997 0 0 0 1.412 0l2.94-2.932 1.574 1.569a1 1 0 0 0 1.23.143c.414-.255.843-.502 1.285-.746.65 3.808-.926 8.176-4.914 13.638a1 1 0 0 0 1.049 1.56c15.94-3.963 18.296-17.609 17.313-21.865a3.142 3.142 0 0 0-.224-.645 21.16 21.16 0 0 0 1.834-1.604C57.103 29.22 64 17.066 64 8.9zM16.058 30.548c-3.902-.823-8.189.32-13.28 3.562 2.504-6.948 7.065-10.23 10.643-11.776 2.682-1.158 5.124-1.483 6.686-1.483.42 0 .774.024 1.054.06l-5.103 9.637zm7.579 18.069-8.412-8.385 2.23-2.221 7.268 7.242 1.144 1.14-2.23 2.224zm17.896 1.955c-1.547 3.583-4.842 8.148-11.837 10.651 3.246-5.069 4.394-9.338 3.57-13.23l9.674-5.089c.174 1.315.047 4.299-1.407 7.668zm-6.844-5.708c-1.758.847-3.433 1.651-4.97 2.544L16.436 34.172c.718-1.229 1.38-2.562 2.052-3.94l4.061-7.667c.85-1.316 1.792-2.551 2.883-3.638C38.984 5.419 54.917-1.523 60.228 3.765 61.404 4.937 62 6.665 62 8.9c0 7.545-6.825 19.417-16.982 29.541-2.83 2.82-6.642 4.653-10.329 6.425z"/><path d="M42.725 12.853a5.953 5.953 0 0 0-1.768 4.248c0 1.607.628 3.116 1.768 4.25a6.023 6.023 0 0 0 4.26 1.753 6.02 6.02 0 0 0 4.26-1.754 5.952 5.952 0 0 0 1.767-4.249 5.952 5.952 0 0 0-1.767-4.248c-2.348-2.338-6.17-2.338-8.52 0zm7.11 7.08a4.048 4.048 0 0 1-5.7 0 3.97 3.97 0 0 1-1.178-2.832 3.97 3.97 0 0 1 1.178-2.83 4.028 4.028 0 0 1 2.85-1.173c1.033 0 2.064.391 2.85 1.173a3.969 3.969 0 0 1 1.177 2.83 3.97 3.97 0 0 1-1.177 2.831zM16.465 47.147a1 1 0 0 0-1.414-.002l-9.995 9.962a1 1 0 1 0 1.412 1.416l9.995-9.962a1 1 0 0 0 .002-1.414zM5.725 51.973a1 1 0 0 0 .706-.292l6.582-6.56a1 1 0 0 0-1.412-1.416l-6.583 6.56a1 1 0 0 0 .707 1.708zM18.502 50.584l-6.582 6.56a1 1 0 0 0 1.412 1.416L19.914 52a1 1 0 0 0-1.412-1.416z"/></svg>

                  </div>
                </div>
                <div className='Prediction-name'>
                  Clacky
                </div>
              </div>
              <div className='Prediction'>
                <div className='Prediction-value'>
                  <div className='Prediction-percentage' id = "thocky"></div>
                  <div className='Prediction-svg'>
                  <svg width="64" height="64" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 59 59" xmlSpace="preserve"><path d="M20.187 28.313a.999.999 0 1 0-1.414 1.414l9.979 9.979c.186.189.44.294.706.294.007 0 .014-.004.021-.004.007 0 .013.004.021.004a.981.981 0 0 0 .795-.423l9.891-9.891a.999.999 0 1 0-1.414-1.414L30.5 36.544V1a1 1 0 1 0-2 0v35.628l-8.313-8.315z"/><path d="M36.5 16a1 1 0 1 0 0 2h13v39h-40V18h13a1 1 0 1 0 0-2h-15v43h44V16h-15z"/></svg>
                  </div>
                </div>
                <div className='Prediction-name'>
                  Thonky
                </div>
              </div>
              <div className='Prediction'>
                <div className='Prediction-value'>
                  <div className='Prediction-percentage' id = "muted"></div>
                  <div className='Prediction-svg'>
                  <svg width="64" height="64"  xmlns="http://www.w3.org/2000/svg" viewBox="0 0 56 56" xmlSpace="preserve"><path d="M25 46H10.845C4.865 46 0 41.135 0 35.154 0 31 2.705 26.688 6.433 24.901L7 24.63V24c0-.127.008-.256.015-.386l.009-.16-.012-.21C7.006 23.163 7 23.082 7 23c0-3.859 3.141-7 7-7a6.995 6.995 0 0 1 1.15.103c.267.044.53.102.789.177.035.01.071.017.106.027.285.087.563.197.835.321.071.032.14.067.21.101A6.995 6.995 0 0 1 21 23a1 1 0 1 0 2 0 8.98 8.98 0 0 0-3.2-6.871C22.667 12.379 27.388 10 32.085 10c7.745 0 14.177 6.135 14.848 13.888-1.022-.072-2.552-.109-4.083.124a1 1 0 0 0 .3 1.977c2.227-.337 4.548-.021 4.684-.002C52.49 26.872 56 31.161 56 35.972 56 41.501 51.501 46 45.972 46H25z"/></svg>                  </div>
                </div>
                <div className='Prediction-name'>
                  Muted
                </div>
              </div>
              <div className='Prediction'>
                <div className='Prediction-value'>
                  <div className='Prediction-percentage' id = "silent"></div>
                  <div className='Prediction-svg'>
                  <svg width="64" height="64" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 319.748 319.748" xmlSpace="preserve"><path d="M192.078 26.649a15.001 15.001 0 0 0-15.398.744L90.458 84.874H15c-8.284 0-15 6.716-15 15v120c0 8.284 6.716 15 15 15h75.458l86.221 57.481a14.993 14.993 0 0 0 15.398.744 14.998 14.998 0 0 0 7.922-13.225v-240a14.997 14.997 0 0 0-7.921-13.225zM170 251.846l-66.68-44.453a14.996 14.996 0 0 0-8.32-2.519H30v-90h65c2.961 0 5.856-.877 8.32-2.519L170 67.902v183.944zM301.212 159.873l14.142-14.142c5.858-5.858 5.858-15.355 0-21.213-5.857-5.858-15.355-5.858-21.213 0l-14.142 14.142-14.142-14.142c-5.857-5.858-15.356-5.858-21.213 0-5.858 5.858-5.858 15.355 0 21.213l14.142 14.142-14.142 14.142c-5.858 5.858-5.858 15.355 0 21.213a14.953 14.953 0 0 0 10.607 4.393 14.95 14.95 0 0 0 10.606-4.393l14.142-14.142 14.142 14.142a14.953 14.953 0 0 0 10.606 4.393 14.95 14.95 0 0 0 10.606-4.393c5.858-5.858 5.858-15.355 0-21.213l-14.141-14.142z"/></svg>
                  </div>
                </div>
                <div className='Prediction-name'>
                  Silent
                </div>
              </div>
            </div>
          </div>

        </div>
      </header>
    </div>
  );
}

export default App;
