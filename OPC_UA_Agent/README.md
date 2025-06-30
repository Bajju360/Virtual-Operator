# OPC_UA_Agent

This folder contains an OPC-UA client that monitors for voice commands and searches for specific tags in an OPC-UA server with audio feedback.

## Features

- **Voice Command Detection**: Monitors for trigger files created by the Netflix subtitle UI
- **Tag Pattern Recognition**: Searches for VP, PT, or Tag followed by numbers in transcribed text
- **OPC-UA Node Search**: Connects to OPC-UA server and searches for matching nodes
- **Value Reading**: Reads and displays values from found nodes
- **Audio Feedback**: Speaks out all operations, search results, and node values
- **Non-blocking Speech**: Uses threaded audio generation for smooth operation

## How it Works

1. **Voice Input**: The Netflix subtitle UI captures speech and creates a trigger file when "roger" is detected
2. **Pattern Extraction**: The OPC-UA client extracts VP, PT, or Tag patterns from the transcribed text
3. **Server Connection**: Connects to the OPC-UA server and searches for matching nodes
4. **Value Reading**: Reads and displays the values of found nodes
5. **Audio Output**: Speaks out all results and operations in real-time

## Audio Features

- **Real-time Feedback**: Speaks out each step of the process
- **Value Announcement**: Announces found node values clearly
- **Error Reporting**: Speaks error messages when issues occur
- **Status Updates**: Announces connection status and search results
- **Configurable**: Adjustable speech rate and volume

## Usage

### Example Voice Commands
- "Check VP 123 roger" → Searches for VP123 and speaks the value
- "Read PT 456 roger" → Searches for PT456 and speaks the value
- "Get Tag 789 roger" → Searches for Tag789 and speaks the value

### Running the Client
```bash
cd OPC_UA_Agent
python opcua_client.py
```

### Audio Configuration
Edit `audio_generator.py` to customize:
- Speech rate (words per minute)
- Volume level
- Voice selection

### Configuration
- Edit the `url` variable in `opcua_client.py` to point to your OPC-UA server
- Default: `opc.tcp://localhost:4840/freeopcua/server/`

## Requirements
- `opcua` Python library (already installed)
- `pyttsx3` Python library (already installed)
- Access to an OPC-UA server
- Netflix subtitle UI running to capture voice input
- Windows audio system (for text-to-speech) 