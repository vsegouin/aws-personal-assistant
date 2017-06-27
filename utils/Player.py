import audio
import speech
import os.path
import configargparse

CONFIG_DIR = os.getenv('XDG_CONFIG_HOME') or os.path.expanduser('~/.config')
CONFIG_FILES = [
    '/etc/voice-recognizer.ini',
    os.path.join(CONFIG_DIR, 'voice-recognizer.ini')
]

def main():
    parser = configargparse.ArgParser(default_config_files=CONFIG_FILES)
    parser.add_argument('-I', '--input-device', default='default',
                           help='Name of the audio input device')
    parser.add_argument('-O', '--output-device', default='default',
                           help='Name of the audio output device')
    parser.add_argument('-T', '--trigger', default='gpio',
                           choices=['clap', 'gpio', 'ok-google'], help='Trigger to use')
    parser.add_argument('--cloud-speech', action='store_true',
                           help='Use the Cloud Speech API instead of the Assistant API')
    parser.add_argument('-L', '--language', default='en-US',
                           help='Language code to use for speech (default: en-US)')
    parser.add_argument('-l', '--led-fifo', default='/tmp/status-led',
                           help='Status led control fifo')
    parser.add_argument('-p', '--pid-file',
                           help='File containing our process id for monitoring')
    parser.add_argument('--audio-logging', action='store_true',
                           help='Log all requests and responses to WAV files in /tmp')
    parser.add_argument('--assistant-always-responds', action='store_true',
                           help='Play Assistant responses for local actions.'
                           ' You should make sure that you have IFTTT applets for'
                           ' your actions to get the correct response, and also'
                           ' that your actions do not call say().')
       parser.add_argument('--assistant-secrets',
                           default=os.path.expanduser('~/assistant.json'),
                           help='Path to client secrets for the Assistant API')
       parser.add_argument('--cloud-speech-secrets',
                           default=os.path.expanduser('~/cloud_speech.json'),
                           help='Path to service account credentials for the '
                           'Cloud Speech API')
       parser.add_argument('--trigger-sound', default=None,
                           help='Sound when trigger is activated (WAV format)')
    args = parser.parse_args()
    player = audio.Player(args.output_device)

    bytes_per_sample = speech.AUDIO_SAMPLE_SIZE
    sample_rate_hz = speech.AUDIO_SAMPLE_RATE_HZ
    player.play_bytes('tell me a story'.encode('utf-8'), sample_width=bytes_per_sample,
                      sample_rate=sample_rate_hz)

if __name__ == '__main__':
    main()
