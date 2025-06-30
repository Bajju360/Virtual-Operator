# RealtimeSTT + OPC-UA Voice Control System

---

## 🙏 Credits & Acknowledgments

- **RealtimeSTT**: This project is built on top of the excellent [RealtimeSTT](https://github.com/Abhishek-Gupta-Dev/RealtimeSTT) open-source speech-to-text system by Abhishek Gupta. All core speech recognition, audio handling, and much of the UI logic are based on the original RealtimeSTT repository.
- **Original Author**: Abhishek Gupta (https://github.com/Abhishek-Gupta-Dev)
- **License**: Please refer to the original RealtimeSTT repository for license and usage terms.

---

## 🚧 Custom Enhancements & Changes

The following enhancements and integrations were carried out on top of the original RealtimeSTT project:

- **Interactive Voice UI**: The Netflix-style subtitle UI was renamed and enhanced as `interactive_voice_ui.py` (desktop) and `interactive_voice_web.py` (web-based) for more intuitive, real-time voice command interaction.
- **OPC-UA Integration**: A new `OPC_UA_Agent` module was added, enabling direct, offline, voice-driven interaction with industrial PLCs and SCADA systems using the OPC-UA protocol.
- **Offline Audio Feedback**: Added a robust, threaded text-to-speech system for real-time spoken feedback of all OPC-UA operations and results.
- **Industrial Use Case Documentation**: Comprehensive documentation and workflow examples for manufacturing, process, and automation industries.
- **Completely Offline Workflow**: All enhancements ensure the system works 100% offline, suitable for air-gapped and secure industrial environments.

---

A complete offline voice-controlled OPC-UA client system that enables hands-free industrial automation monitoring and control through natural speech commands.

## 🏭 Industrial Use Cases

### **Manufacturing & Process Industries**
- **Chemical Plants**: Voice commands to check pressure (PT), temperature (VP), and valve positions
- **Pharmaceutical**: Monitor critical parameters without touching contaminated surfaces
- **Food & Beverage**: Check tank levels, flow rates, and process temperatures
- **Oil & Gas**: Monitor pipeline pressures, flow rates, and safety systems
- **Power Plants**: Check turbine speeds, generator outputs, and grid parameters

### **Automotive & Assembly**
- **Production Lines**: Voice-activated quality control checks and parameter monitoring
- **Robotics**: Check robot status, position feedback, and safety systems
- **Welding Operations**: Monitor current, voltage, and gas flow rates
- **Paint Shops**: Check temperature, humidity, and air flow parameters

### **Water & Wastewater Treatment**
- **Pump Stations**: Monitor pump status, flow rates, and tank levels
- **Treatment Plants**: Check chemical dosing, pH levels, and turbidity
- **Distribution Networks**: Monitor pressure zones and valve positions

### **Building Automation**
- **HVAC Systems**: Check temperature, humidity, and air flow parameters
- **Energy Management**: Monitor power consumption and efficiency metrics
- **Security Systems**: Check access control and surveillance status

### **Mining & Heavy Industry**
- **Conveyor Systems**: Monitor speed, load, and safety interlocks
- **Crushers & Mills**: Check motor currents, temperatures, and vibration
- **Material Handling**: Monitor hopper levels and transfer rates

## 🖼️ Interactive Voice UI Screenshots

### Desktop Interactive Voice UI
![Interactive Voice UI](screenshots/interactive_voice_ui.png)
*The desktop interactive voice interface showing real-time transcription and voice command controls*

### Web-based Interactive Voice UI
![Interactive Voice Web UI](screenshots/interactive_voice_web.png)
*The web-based interactive voice interface with modern design and real-time updates*

---

## 🔧 System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    COMPLETE SYSTEM OVERVIEW                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  🎤 Voice Input → 📝 Transcription → 🔍 Pattern Recognition    │
│         ↓              ↓                    ↓                   │
│  Interactive UI      Trigger File        OPC-UA Client             │
│         ↓              ↓                    ↓                   │
│  Real-time STT   Text Processing     Tag Extraction            │
│         ↓              ↓                    ↓                   │
│  "roger" Detect   Full Text Save     VP/PT/Tag Search          │
│         ↓              ↓                    ↓                   │
│  File Creation    UTF-8 Encoding     Node Discovery            │
│         ↓              ↓                    ↓                   │
│  Trigger Signal   Complete History   Value Reading             │
│         ↓              ↓                    ↓                   │
│  Audio Feedback   Offline Storage    🔊 Voice Output           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 🚀 Key Features

### **Complete Offline Operation**
- ✅ **No Internet Required**: All components work offline
- ✅ **Local Speech Recognition**: Uses Faster Whisper for real-time transcription
- ✅ **Local Text-to-Speech**: Uses pyttsx3 for voice feedback
- ✅ **Local OPC-UA Client**: Direct connection to industrial servers
- ✅ **No Cloud Dependencies**: Zero external service requirements

### **Voice Command System**
- ✅ **Natural Language**: "Check VP 123 roger" or "Read PT 456 roger"
- ✅ **Pattern Recognition**: Automatically detects VP, PT, and Tag patterns
- ✅ **Number Extraction**: Extracts tag numbers from speech
- ✅ **Multi-tag Support**: Process multiple tags in one command

### **Industrial Integration**
- ✅ **OPC-UA Protocol**: Industry-standard communication
- ✅ **Node Discovery**: Automatic search through server nodes
- ✅ **Value Reading**: Real-time parameter monitoring
- ✅ **Error Handling**: Robust connection and operation management

### **Audio Feedback System**
- ✅ **Real-time Announcements**: Speaks all operations and results
- ✅ **Value Announcements**: Clearly states found values
- ✅ **Status Updates**: Connection and search status
- ✅ **Error Reporting**: Voice error messages
- ✅ **Configurable Speech**: Adjustable rate and volume

## 📁 Project Structure

```
RealtimeSTT-master/
├── README.md                           # This comprehensive guide
├── OPC_UA_Agent/                       # OPC-UA voice control system
│   ├── __init__.py                     # Python package
│   ├── opcua_client.py                 # Main OPC-UA client with voice
│   ├── audio_generator.py              # Text-to-speech engine
│   ├── test_audio.py                   # Audio system test
│   └── README.md                       # OPC-UA specific documentation
└── RealtimeSTT/
    ├── tests/
    │   ├── Interactive_subtitles_ui.py     # Desktop voice UI (modified)
    │   ├── Interactive_subtitles_web.py    # Web-based voice UI
    │   └── realtimestt_test.py         # Basic STT test
    └── [other RealtimeSTT files]
```

## 🛠️ Installation & Setup

### **Prerequisites**
- Python 3.10 or 3.11 (TensorFlow compatibility)
- Windows 10/11 with audio system
- Access to OPC-UA server (industrial equipment)

### **Dependencies Installation**
```bash
# Core dependencies (already installed)
pip install opcua pyttsx3 flask flask-socketio

# RealtimeSTT dependencies
pip install -e RealtimeSTT-master/RealtimeSTT
```

### **System Configuration**
1. **OPC-UA Server URL**: Edit `OPC_UA_Agent/opcua_client.py`
   ```python
   url = "opc.tcp://your-server-ip:4840/your-server-path/"
   ```

2. **Audio Settings**: Edit `OPC_UA_Agent/audio_generator.py`
   ```python
   voice_rate=150    # Words per minute
   voice_volume=0.9  # Volume level (0.0 to 1.0)
   ```

## 🎯 Usage Examples

### **Basic Voice Commands**
```bash
# Check a single tag
"Check VP 123 roger"

# Read multiple tags
"Read PT 456 and Tag 789 roger"

# Monitor process parameters
"Check temperature VP 101 and pressure PT 202 roger"
```

### **Industrial Scenarios**

#### **Chemical Plant Operator**
```bash
# Monitor reactor conditions
"Check reactor temperature VP 101 and pressure PT 202 roger"
# System responds: "VP 101 value is 185.5 degrees Celsius, PT 202 value is 2.3 bar"

# Check safety systems
"Verify safety valve Tag 301 status roger"
# System responds: "Tag 301 value is Open"
```

#### **Power Plant Technician**
```bash
# Monitor turbine parameters
"Check turbine speed VP 501 and generator output PT 502 roger"
# System responds: "VP 501 value is 3000 RPM, PT 502 value is 500 MW"

# Check cooling systems
"Monitor cooling water temperature VP 601 roger"
# System responds: "VP 601 value is 45.2 degrees Celsius"
```

#### **Water Treatment Operator**
```bash
# Check treatment parameters
"Monitor pH level VP 701 and chlorine PT 702 roger"
# System responds: "VP 701 value is 7.2, PT 702 value is 2.1 mg/L"

# Check pump status
"Verify pump Tag 801 status roger"
# System responds: "Tag 801 value is Running"
```

## 🔄 Complete Workflow

### **1. System Startup**
```bash
# Terminal 1: Start OPC-UA client
cd RealtimeSTT-master/OPC_UA_Agent
python opcua_client.py
# Audio: "OPC-UA client started. Monitoring for voice commands."

# Terminal 2: Start voice UI
cd RealtimeSTT-master/RealtimeSTT
python tests/Interactive_subtitles_ui.py
```

### **2. Voice Command Processing**
1. **Speech Input**: Operator speaks "Check VP 123 roger"
2. **Real-time Transcription**: Interactive UI captures and displays text
3. **Pattern Detection**: "roger" triggers file creation
4. **Text Processing**: OPC-UA client reads full transcription
5. **Tag Extraction**: Identifies "VP 123" pattern
6. **Server Connection**: Connects to OPC-UA server
7. **Node Search**: Searches for "VP123" in server nodes
8. **Value Reading**: Reads found node values
9. **Audio Feedback**: Speaks results to operator

### **3. Audio Response Example**
```
🔊 "Voice command detected. Processing transcription."
🔊 "Analyzing transcription for VP, PT, or Tag patterns"
🔊 "Found VP 123"
🔊 "Searching for nodes containing VP123"
🔊 "Found matching node VP123_Temperature"
🔊 "Node VP123_Temperature value is 185.5"
🔊 "Found 1 matching node(s) for 1 tag(s)"
🔊 "OPC-UA operations completed"
```

## 🔧 Technical Implementation

### **Voice Recognition (RealtimeSTT)**
- **Model**: Faster Whisper (tiny model for speed)
- **Language**: Auto-detection (supports multiple languages)
- **Latency**: Real-time with minimal delay
- **Accuracy**: High accuracy for industrial terminology

### **OPC-UA Integration**
- **Protocol**: OPC-UA (OPC Unified Architecture)
- **Connection**: TCP/IP to industrial servers
- **Security**: Supports various security modes
- **Discovery**: Automatic node browsing and search
- **Data Types**: Handles all OPC-UA data types

### **Audio Generation**
- **Engine**: pyttsx3 (cross-platform TTS)
- **Threading**: Non-blocking speech queue
- **Customization**: Adjustable rate, volume, and voice
- **Error Handling**: Graceful failure management

## 🏭 Industrial Benefits

### **Safety & Efficiency**
- **Hands-free Operation**: No need to touch contaminated surfaces
- **Reduced Errors**: Voice confirmation prevents misreading
- **Faster Response**: Immediate parameter checking
- **24/7 Availability**: Works in all lighting conditions

### **Cost Savings**
- **Reduced Training**: Natural language commands
- **Faster Operations**: Quick parameter access
- **Error Prevention**: Audio confirmation reduces mistakes
- **Offline Operation**: No cloud service costs

### **Compliance & Documentation**
- **Audit Trail**: All commands and responses logged
- **Standard Protocols**: Uses industry-standard OPC-UA
- **Secure Communication**: Direct server connections
- **Data Integrity**: Real-time value verification

## 🔒 Security & Reliability

### **Offline Security**
- **No Internet Exposure**: Complete air-gap capability
- **Direct Connections**: No intermediate servers
- **Local Processing**: All data stays on-premises
- **Industrial Standards**: Uses proven OPC-UA protocol

### **Reliability Features**
- **Error Recovery**: Automatic reconnection attempts
- **Graceful Degradation**: Continues operation with partial failures
- **Logging**: Comprehensive operation logging
- **Backup Systems**: Can work with multiple OPC-UA servers

## 🚀 Future Enhancements

### **Planned Features**
- **Multi-language Support**: International industrial deployments
- **Advanced Commands**: Complex parameter calculations
- **Trend Analysis**: Historical data voice queries
- **Alarm Integration**: Voice alarm announcements
- **Mobile Support**: Tablet/phone voice interfaces

### **Integration Possibilities**
- **SCADA Systems**: Direct SCADA integration
- **MES Systems**: Manufacturing execution system links
- **ERP Systems**: Enterprise resource planning integration
- **IoT Platforms**: Internet of Things connectivity
- **AI/ML**: Predictive maintenance integration

## 📞 Support & Documentation

### **Testing Your System**
```bash
# Test audio system
cd RealtimeSTT-master/OPC_UA_Agent
python test_audio.py

# Test basic STT
cd RealtimeSTT-master/RealtimeSTT
python tests/realtimestt_test.py

# Test complete system
# Follow the usage examples above
```

### **Troubleshooting**
- **Audio Issues**: Check Windows audio settings and pyttsx3 installation
- **OPC-UA Connection**: Verify server URL and network connectivity
- **Speech Recognition**: Ensure clear microphone and quiet environment
- **Performance**: Adjust speech rate and audio settings as needed

## 📄 License & Acknowledgments

- **RealtimeSTT**: Original speech recognition system
- **OPC-UA**: Industry standard protocol
- **pyttsx3**: Text-to-speech engine
- **Faster Whisper**: Speech recognition model

---

**This system represents a complete offline voice control solution for industrial automation, providing hands-free operation with full audio feedback while maintaining the highest standards of security and reliability for industrial environments.**