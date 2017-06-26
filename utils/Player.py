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
    parser.add_argument('--assistant-secrets',
                            default=os.path.expanduser('~/assistant.json'),
                            help='Path to client secrets for the Assistant API')
    args = parser.parse_args()
    player = audio.Player(args.output_device)

    bytes_per_sample = speech.AUDIO_SAMPLE_SIZE
    sample_rate_hz = speech.AUDIO_SAMPLE_RATE_HZ
    player.play_bytes('tell me a story'.encode('utf-8'), sample_width=bytes_per_sample,
                      sample_rate=sample_rate_hz)

if __name__ == '__main__':
    main()
