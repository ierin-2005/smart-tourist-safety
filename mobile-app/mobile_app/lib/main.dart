import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(const TouristApp());
}

class TouristApp extends StatelessWidget {
  const TouristApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Tourist Safety',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const TouristHomePage(),
    );
  }
}

class TouristHomePage extends StatefulWidget {
  const TouristHomePage({super.key});

  @override
  State<TouristHomePage> createState() => _TouristHomePageState();
}

class _TouristHomePageState extends State<TouristHomePage> {
  final TextEditingController nameController = TextEditingController();
  final TextEditingController docController = TextEditingController();

  // Use your PC’s local IP for real phone
  String apiUrl = "http://192.168.1.3:8000";
  String responseMsg = "";

  Future<void> registerTourist() async {
    var url = Uri.parse("$apiUrl/tourists/");
    var body = {
      "digital_id": DateTime.now().millisecondsSinceEpoch.toString(),
      "name": nameController.text,
      "passport_or_aadhaar": docController.text,
      "phone": "9876543210",
      "emergency_contact": "9876500000"
    };

    try {
      var res = await http.post(url,
          headers: {"Content-Type": "application/json"},
          body: json.encode(body));

      setState(() {
        responseMsg = res.body;
      });
    } catch (e) {
      setState(() {
        responseMsg = "Error: $e";
      });
    }
  }

  Future<void> sendPanic() async {
    var url = Uri.parse("$apiUrl/alerts/");
    var body = {
      "tourist_id": 1,
      "trip_id": 1,
      "alert_type": "panic",
      "description": "Tourist pressed panic button",
      "location": "Test Location"
    };

    try {
      var res = await http.post(url,
          headers: {"Content-Type": "application/json"},
          body: json.encode(body));

      setState(() {
        responseMsg = res.body;
      });
    } catch (e) {
      setState(() {
        responseMsg = "Error: $e";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Tourist Safety App")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: nameController,
              decoration: const InputDecoration(labelText: "Name"),
            ),
            TextField(
              controller: docController,
              decoration: const InputDecoration(labelText: "Passport/Aadhaar"),
            ),
            const SizedBox(height: 10),
            ElevatedButton(
                onPressed: registerTourist,
                child: const Text("Register Tourist")),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: sendPanic,
              style: ElevatedButton.styleFrom(backgroundColor: Colors.red),
              child: const Text("🚨 Panic Button"),
            ),
            const SizedBox(height: 20),
            Text("Response: $responseMsg"),
          ],
        ),
      ),
    );
  }
}
